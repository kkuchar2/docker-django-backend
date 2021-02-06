from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string

from settings import settings


class AccountAdapter(DefaultAccountAdapter):

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        key = emailconfirmation.key
        emailaddress = emailconfirmation.email_address

        activate_url = settings.URL_FRONT + 'verify-email/' + key

        ctx = {
            "user": emailaddress.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": key,
        }

        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation"

        self.send_mail(email_template, emailaddress.email, ctx)

    def respond_email_verification_sent(self, request, user):
        return HttpResponse('')

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        email = data.get("email")
        user_email(user, email)
        user.set_password(data["password"])
        self.populate_username(request, user)
        user.save()
        return user

    def render_mail(self, template_prefix, email, context):
        to = [email] if isinstance(email, str) else email
        subject = render_to_string("{0}_subject.txt".format(template_prefix), context)

        subject = " ".join(subject.splitlines()).strip()
        subject = self.format_email_subject(subject)

        from_email = self.get_from_email()

        bodies = {}

        for ext in ["html", "txt"]:
            try:
                template_name = "{0}_message.{1}".format(template_prefix, ext)
                bodies[ext] = render_to_string(template_name, context, self.request).strip()

            except TemplateDoesNotExist:
                if ext == "txt" and not bodies:
                    raise

        if "txt" in bodies:
            msg = EmailMultiAlternatives(subject, bodies["txt"], from_email, to)
            if "html" in bodies:
                msg.attach_alternative(bodies["html"], "text/html")
        else:
            msg = EmailMessage(subject, bodies["html"], from_email, to)
            msg.content_subtype = "html"
        return msg
