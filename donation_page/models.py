import enum

from django.db import models
from django.urls import reverse


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
    viewer_pays_commision = models.BooleanField(default=True, verbose_name="Глядач платить комісію")
    commision_percent = models.FloatField(default=0.5, verbose_name="Комісія від суми")
    page_link = models.CharField(max_length=255, verbose_name="Посилання на сторінку")
    page_title = models.CharField(max_length=255, default="Скинути Грошик", verbose_name="Заголовок сторінки")
    page_meta = models.CharField(max_length=512, null=True, blank=True, verbose_name="Мета теги сторінки")
    title = models.CharField(max_length=255, default="Скинути Грошик Стрімеру", verbose_name="Заголовок привітання")
    title_subtext = models.CharField(
        max_length=255,
        default="Скинь Грошик цьому стрімеру",
        verbose_name="Підзаголовок привітання",
    )
    nickname_placeholder = models.CharField(max_length=64, default="Нікнейм", verbose_name="Плейсхолдер нікнейму")
    amount_placeholder = models.CharField(max_length=32, default="Сума", verbose_name="Плейсхолдер суми")
    message_placeholder = models.CharField(
        max_length=255,
        default="Повідомлення",
        verbose_name="Плейсхолдер повідомлення",
    )
    donate_button_text = models.CharField(max_length=32, default="Скинути Грошик", verbose_name="Текст кнопки подяки")
    test_mode = models.BooleanField(default=False, verbose_name="Тестовий режим")
    message_min_length = models.IntegerField(default=0, verbose_name="Мінімальна довжина повідомлення")
    message_max_length = models.IntegerField(default=333, verbose_name="Максимальна довжина повідомлення")
    nickname_min_length = models.IntegerField(default=1, verbose_name="Мінімальна довжина нікнейму")
    nickname_max_length = models.IntegerField(default=69, verbose_name="Максимальна довжина нікнейму")
    amount_min = models.IntegerField(default=1, verbose_name="Мінімальна сума")
    amount_max = models.IntegerField(default=10000, verbose_name="Максимальна сума")
    target_title = models.CharField(max_length=255, default="На хаймарс", verbose_name="Заголовок цілі")
    target_amount = models.IntegerField(default=10000, verbose_name="Сума цілі")
    target_current_amount = models.IntegerField(default=0, verbose_name="Зібрано грошей")

    widgets = models.ManyToManyField(
        Widget,
        related_name="donation_pages",
        verbose_name="Віджети",
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("donation_page")

    def reset_current_target(self):
        self.target_current_amount = 0
        self.save()
