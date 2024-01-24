from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class DonationPage(models.Model):
    viewer_pays_commission = models.BooleanField(default=True, verbose_name=_("Viewer pays a commission"))
    commission_percent = models.FloatField(default=0.5, verbose_name=_("Commission percent"))
    page_link = models.CharField(max_length=255, unique=True, verbose_name=_("Page link"))
    page_title = models.CharField(
        max_length=255,
        default=_("Send Hroshyk"),
        verbose_name=_("Page title"),
    )
    page_meta = models.CharField(max_length=512, null=True, blank=True, verbose_name=_("Page meta description"))
    title = models.CharField(
        max_length=255,
        default=_("Send Hroshyk to the streamer"),
        verbose_name=_("Greeting title"),
    )
    title_subtext = models.CharField(
        max_length=255,
        default=_("Send Hroshyk to this streamer"),
        verbose_name=_("Greeting subtext"),
    )
    nickname_placeholder = models.CharField(
        max_length=64,
        default=_("Nickname"),
        verbose_name=_("Nickname placeholder"),
    )
    amount_placeholder = models.CharField(
        max_length=32,
        default=_("Amount"),
        verbose_name=_("Amount placeholder"),
    )
    message_placeholder = models.CharField(
        max_length=255,
        default=_("Message"),
        verbose_name=_("Message placeholder"),
    )
    donate_button_text = models.CharField(
        max_length=32,
        default=_("Send Hroshyk"),
        verbose_name=_("Donation button text"),
    )
    test_mode = models.BooleanField(default=False, verbose_name=_("Test mode"))
    message_min_length = models.IntegerField(default=0, verbose_name=_("Minimum message length"))
    message_max_length = models.IntegerField(default=333, verbose_name=_("Maximum message length"))
    nickname_min_length = models.IntegerField(default=1, verbose_name=_("Minimum nickname length"))
    nickname_max_length = models.IntegerField(default=69, verbose_name=_("Maximum nickname length"))
    amount_min = models.IntegerField(default=1, verbose_name=_("Minimum amount"))
    amount_max = models.IntegerField(default=10000, verbose_name=_("Maximum amount"))
    target_title = models.CharField(
        max_length=255,
        default=_("Donation target"),
        verbose_name=_("Donation target title"),
    )
    target_amount = models.IntegerField(default=10000, verbose_name=_("Donation target amount"))
    target_current_amount = models.IntegerField(default=0, verbose_name=_("Donation target current amount"))

    def get_absolute_url(self):
        return reverse("donation_page")

    def reset_current_target(self):
        self.target_current_amount = 0
        self.save()
