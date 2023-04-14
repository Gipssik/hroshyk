from django.db import models


class Donation(models.Model):
    nickname = models.CharField(max_length=128)
    amount = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nickname} ({self.amount})"
