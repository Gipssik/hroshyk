from django.contrib.auth.base_user import BaseUserManager

from accounts.utils import hash_password
from donation_page.models import DonationPage


class StreamerManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            password = self.make_random_password()
        password = hash_password(password)
        new_user = self.model(
            username=username,
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False,
            **extra_fields,
        )
        new_user.save()
        donation_page = DonationPage.objects.create(page_link=username)
        donation_page.save()
        new_user.donation_page = donation_page
        new_user.save()
        return new_user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Superusers must have a password")
        password = hash_password(password)
        new_user = self.model(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )
        new_user.save()
        return new_user
