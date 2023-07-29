from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.manager import StreamerManager
from accounts.utils import hash_password, check_password

from donation_page.models import DonationPage


class Streamer(AbstractUser):
    email = models.EmailField(_("email address"), null=True, blank=True)
    auth_id = models.IntegerField(null=True, blank=True)
    profile_image_url = models.CharField(max_length=512, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    donation_page = models.OneToOneField(DonationPage, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = []

    objects = StreamerManager()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = hash_password(raw_password)
        self._password = raw_password
