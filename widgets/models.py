import secrets

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models


def generate_link_identifier():
    return secrets.token_urlsafe(90)


class BaseWidget(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва віджета")
    link_identifier = models.CharField(
        max_length=128,
        unique=True,
        default=generate_link_identifier,
        verbose_name="Посилання на віджет",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    class Meta:
        abstract = True


class DonationWidgetConfig(models.Model):
    title_format = models.CharField(max_length=255, default="{nickname} - {amount}", verbose_name="Формат заголовку")
    min_amount = models.IntegerField(default=20, verbose_name="Мінімальна сума для відображення")
    max_amount = models.IntegerField(default=10000, verbose_name="Максимальна сума для відображення")
    title_font_size = models.IntegerField(default=24, verbose_name="Розмір шрифту заголовку")
    title_color = models.CharField(max_length=7, default="#ffffff", verbose_name="Колір заголовку")
    title_shadow_color = models.CharField(max_length=7, default="#000000", verbose_name="Колір тіні заголовку")
    message_font_size = models.IntegerField(default=20, verbose_name="Розмір шрифту повідомлення")
    message_color = models.CharField(max_length=7, default="#ffffff", verbose_name="Колір повідомлення")
    message_shadow_color = models.CharField(max_length=7, default="#000000", verbose_name="Колір тіні повідомлення")
    image = models.ImageField(upload_to="donation_widget/images/", verbose_name="Зображення")
    sound = models.FileField(
        upload_to="donation_widget/sounds/",
        verbose_name="Мелодія",
        storage=RawMediaCloudinaryStorage(),
    )
    sound_volume = models.IntegerField(default=100, verbose_name="Гучність мелодії")
    speaker_volume = models.IntegerField(default=100, verbose_name="Гучність спікера")
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
