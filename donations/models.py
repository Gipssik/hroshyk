from django.db import models


class Donation(models.Model):
    nickname = models.CharField(max_length=128, verbose_name="Нікнейм")
    amount = models.IntegerField(verbose_name="Кількість")
    message = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nickname} ({self.amount})"
