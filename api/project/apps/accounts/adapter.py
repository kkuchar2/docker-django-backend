from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email
from django.http import HttpResponse


class AccountAdapter(DefaultAccountAdapter):
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
