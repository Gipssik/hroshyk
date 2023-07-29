from django.db import models
from django.urls import reverse_lazy

from accounts.models import Streamer


class Donation(models.Model):
    nickname = models.CharField(max_length=128, verbose_name="Нікнейм")
    amount = models.IntegerField(verbose_name="Кількість")
    message = models.TextField(verbose_name="Повідомлення", null=True, blank=True)
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nickname} ({self.amount})"

    def get_absolute_url(self):
        return reverse_lazy("viewer_donation_page", kwargs={"link": self.streamer.donation_page.page_link})
