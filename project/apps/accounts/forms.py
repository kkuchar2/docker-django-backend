from django.conf import settings
from django.contrib.auth import (get_user_model, )
from django.contrib.sites.shortcuts import get_current_site
from django.forms import ModelForm

from settings import settings

if 'allauth' in settings.INSTALLED_APPS:
    from allauth.account import app_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.forms import \
        ResetPasswordForm as DefaultPasswordResetForm
    from allauth.account.forms import default_token_generator
    from allauth.account.utils import (filter_users_by_email,
                                       user_pk_to_url_str, user_username)
else:
    from django.contrib.auth.forms import PasswordResetForm as DefaultPasswordResetForm
    from django.contrib.auth.tokens import default_token_generator

UserModel = get_user_model()

'''
 subject_template_name='account/email/forgot_password/password_reset_email_subject.txt',
             email_template_name='account/email/forgot_password/password_reset_email_message.html',
             html_email_template_name='account/email/forgot_password/password_reset_email_message.html',
'''


class PasswordResetForm(DefaultPasswordResetForm):
    def clean_email(self):
        """
        Invalid email should not raise error, as this would leak users
        for unit test: test_password_reset_with_invalid_email
        """
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = filter_users_by_email(email, is_active=True)
        return self.cleaned_data["email"]

    def save(self, request, **kwargs):
        if 'allauth' not in settings.INSTALLED_APPS:
            return super().save(request, **kwargs)
        # for allauth
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': settings.URL_FRONT + 'resetPassword/' + user_pk_to_url_str(user) + ":" + temp_key,
                'request': request,
            }
            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/forgot_password/password_reset_email', email, context
            )
        return self.cleaned_data['email']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('avatar',)
