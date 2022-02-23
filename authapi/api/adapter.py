from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_field, user_username
from allauth.utils import valid_email_or_none

class UserAccountCustomAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        """
        Hook that can be used to further populate the user instance.
        For convenience, we populate several common fields.
        Note that the user instance being populated represents a
        suggested User instance that represents the social user that is
        in the process of being logged in.
        The User instance need not be completely valid and conflict
        free. For example, verifying whether or not the username
        already exists, is not a responsibility.
        """
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        name = data.get("name")
        image_url = sociallogin.account.extra_data.get('picture')
        """
        Check Email Domain is accubits.com
        """
        email_domain = email.split('@')[1]
        allowed_domain = 'accubits.com'
        if not email_domain == allowed_domain:
            raise ValidationError(email + ' is not a valid member of ' + allowed_domain)

        user = sociallogin.user
        user_username(user, username or "")
        user_email(user, valid_email_or_none(email) or "")
        name_parts = (name or "").partition(" ")
        user_field(user, "first_name", first_name or name_parts[0])
        user_field(user, "last_name", last_name or name_parts[2])
        """
        Add social avatar to User instance
        """
        user_field(user, "image_url", image_url)
        
        return user