import secrets

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models
from django.utils.translation import gettext_lazy as _


def generate_link_identifier():
    return secrets.token_urlsafe(90)


class BaseWidget(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Widget name"))
    link_identifier = models.CharField(
        max_length=128,
        unique=True,
        default=generate_link_identifier,
        verbose_name=_("Widget link"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation date"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Update date"))

    class Meta:
        abstract = True


class DonationWidgetConfig(models.Model):
    title_format = models.CharField(max_length=255, default="{nickname} - {amount}", verbose_name=_("Title format"))
    min_amount = models.IntegerField(default=20, verbose_name=_("Minimum amount to display"))
    max_amount = models.IntegerField(default=10000, verbose_name=_("Maximum amount to display"))
    title_font_size = models.IntegerField(default=24, verbose_name=_("Title font size"))
    title_color = models.CharField(max_length=7, default="#ffffff", verbose_name=_("Title color"))
    title_shadow_color = models.CharField(max_length=7, default="#000000", verbose_name=_("Title shadow color"))
    message_font_size = models.IntegerField(default=20, verbose_name=_("Message font size"))
    message_color = models.CharField(max_length=7, default="#ffffff", verbose_name=_("Message color"))
    message_shadow_color = models.CharField(max_length=7, default="#000000", verbose_name=_("Message shadow color"))
    image = models.ImageField(upload_to="donation_widget/images/", verbose_name=_("Image"))
    sound = models.FileField(
        upload_to="donation_widget/sounds/",
        verbose_name=_("Sound"),
        storage=RawMediaCloudinaryStorage(),
    )
    sound_volume = models.IntegerField(default=100, verbose_name=_("Sound volume"))
    speaker_volume = models.IntegerField(default=100, verbose_name=_("Speaker volume"))
    donation_widget = models.ForeignKey(
        "widgets.DonationWidget",
        on_delete=models.CASCADE,
        related_name="configs",
    )

    def __str__(self):
        return f"{self.donation_widget.name} - Config {self.pk}"


class DonationWidget(BaseWidget):
    user = models.ForeignKey("accounts.Streamer", on_delete=models.CASCADE, related_name="donation_widgets")

    def __str__(self):
        return f"{self.name} ({self.pk})"
