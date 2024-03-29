# Generated by Django 4.1.6 on 2023-02-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Widget",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Віджет", max_length=255)),
                (
                    "amount_of_ranks",
                    models.IntegerField(blank=True, default=5, null=True),
                ),
                (
                    "ranking_type",
                    models.CharField(
                        blank=True,
                        choices=[("TOP", "TOP"), ("LAST", "LAST")],
                        default="TOP",
                        max_length=64,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DonationPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("viewer_pays_commision", models.BooleanField(default=True)),
                ("commision_percent", models.FloatField(default=0.5)),
                ("page_link", models.CharField(max_length=255)),
                (
                    "page_title",
                    models.CharField(default="Скинути Грошик", max_length=255),
                ),
                ("page_meta", models.CharField(blank=True, max_length=512, null=True)),
                (
                    "title",
                    models.CharField(default="Скинути Грошик Стрімеру", max_length=255),
                ),
                (
                    "title_subtext",
                    models.CharField(
                        default="Скинь Грошик цьому стрімеру", max_length=255
                    ),
                ),
                (
                    "nickname_placeholder",
                    models.CharField(default="Нікнейм", max_length=64),
                ),
                ("amount_placeholder", models.CharField(default="Сума", max_length=32)),
                (
                    "message_placeholder",
                    models.CharField(default="Повідомлення", max_length=255),
                ),
                (
                    "donate_button_text",
                    models.CharField(default="Скинути Грошик", max_length=32),
                ),
                ("test_mode", models.BooleanField(default=False)),
                ("message_min_length", models.IntegerField(default=0)),
                ("message_max_length", models.IntegerField(default=333)),
                ("nickname_min_length", models.IntegerField(default=1)),
                ("nickname_max_length", models.IntegerField(default=69)),
                ("amount_min", models.IntegerField(default=1)),
                ("amount_max", models.IntegerField(default=10000)),
                (
                    "target_title",
                    models.CharField(default="Ціль. Зібрано {} грн", max_length=255),
                ),
                ("target_amount", models.IntegerField(default=10000)),
                (
                    "widgets",
                    models.ManyToManyField(
                        related_name="donation_pages", to="donation_page.widget"
                    ),
                ),
            ],
        ),
    ]
