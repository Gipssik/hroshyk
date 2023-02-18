import enum

from django.db import models


class ChoicesEnum(enum.Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Ranking(ChoicesEnum):
    TOP = "TOP"
    LAST = "LAST"


class Widget(models.Model):
    title = models.CharField(max_length=255, default="Віджет")
    amount_of_ranks = models.IntegerField(default=5, null=True, blank=True)
    ranking_type = models.CharField(
        max_length=64,
        choices=Ranking.choices(),
        default=Ranking.TOP.name,
        null=True,
        blank=True,
    )


class DonationPage(models.Model):
    viewer_pays_commision = models.BooleanField(default=True)
    commision_percent = models.FloatField(default=0.5)
    page_link = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255, default="Скинути Грошик")
    page_meta = models.CharField(max_length=512, null=True, blank=True)
    title = models.CharField(max_length=255, default="Скинути Грошик Стрімеру")
    title_subtext = models.CharField(max_length=255, default="Скинь Грошик цьому стрімеру")
    nickname_placeholder = models.CharField(max_length=64, default="Нікнейм")
    amount_placeholder = models.CharField(max_length=32, default="Сума")
    message_placeholder = models.CharField(max_length=255, default="Повідомлення")
    donate_button_text = models.CharField(max_length=32, default="Скинути Грошик")
    test_mode = models.BooleanField(default=False)
    message_min_length = models.IntegerField(default=0)
    message_max_length = models.IntegerField(default=333)
    nickname_min_length = models.IntegerField(default=1)
    nickname_max_length = models.IntegerField(default=69)
    amount_min = models.IntegerField(default=1)
    amount_max = models.IntegerField(default=10000)
    target_title = models.CharField(max_length=255, default="Ціль. Зібрано {} грн")
    target_amount = models.IntegerField(default=10000)

    widgets = models.ManyToManyField(Widget, related_name="donation_pages")
