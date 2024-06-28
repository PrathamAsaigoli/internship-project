# Generated by Django 5.0.6 on 2024-06-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=255)),
                ("quantity", models.CharField(max_length=255)),
                ("price", models.CharField(max_length=255)),
                (
                    "img",
                    models.ImageField(
                        default=None, max_length=250, null=True, upload_to="media"
                    ),
                ),
            ],
        ),
    ]
