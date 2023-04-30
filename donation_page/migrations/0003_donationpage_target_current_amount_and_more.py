# Generated by Django 4.1.6 on 2023-04-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donation_page", "0002_alter_donationpage_amount_max_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="donationpage",
            name="target_current_amount",
            field=models.IntegerField(default=0, verbose_name="Зібрано грошей"),
        ),
        migrations.AlterField(
            model_name="donationpage",
            name="widgets",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="donation_pages",
                to="donation_page.widget",
                verbose_name="Віджети",
            ),
        ),
    ]