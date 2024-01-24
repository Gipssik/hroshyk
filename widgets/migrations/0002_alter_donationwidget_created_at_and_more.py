# Generated by Django 4.1.6 on 2024-01-24 00:48

import cloudinary_storage.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import widgets.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("widgets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donationwidget",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="donationwidget",
            name="link_identifier",
            field=models.CharField(
                default=widgets.models.generate_link_identifier,
                max_length=128,
                unique=True,
                verbose_name="Widget link",
            ),
        ),
        migrations.AlterField(
            model_name="donationwidget",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Widget name"),
        ),
        migrations.AlterField(
            model_name="donationwidget",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Update date"),
        ),
        migrations.AlterField(
            model_name="donationwidget",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="donation_widgets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="image",
            field=models.ImageField(
                upload_to="donation_widget/images/", verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="max_amount",
            field=models.IntegerField(
                default=10000, verbose_name="Maximum amount to display"
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="message_color",
            field=models.CharField(
                default="#ffffff", max_length=7, verbose_name="Message color"
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="message_font_size",
            field=models.IntegerField(default=20, verbose_name="Message font size"),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="message_shadow_color",
            field=models.CharField(
                default="#000000", max_length=7, verbose_name="Message shadow color"
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="min_amount",
            field=models.IntegerField(
                default=20, verbose_name="Minimum amount to display"
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="sound",
            field=models.FileField(
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="donation_widget/sounds/",
                verbose_name="Sound",
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="sound_volume",
            field=models.IntegerField(default=100, verbose_name="Sound volume"),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="speaker_volume",
            field=models.IntegerField(default=100, verbose_name="Speaker volume"),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="title_color",
            field=models.CharField(
                default="#ffffff", max_length=7, verbose_name="Title color"
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="title_font_size",
            field=models.IntegerField(default=24, verbose_name="Title font size"),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="title_format",
            field=models.CharField(
                default="{nickname} - {amount}",
                max_length=255,
                verbose_name="Title format",
            ),
        ),
        migrations.AlterField(
            model_name="donationwidgetconfig",
            name="title_shadow_color",
            field=models.CharField(
                default="#000000", max_length=7, verbose_name="Title shadow color"
            ),
        ),
    ]
