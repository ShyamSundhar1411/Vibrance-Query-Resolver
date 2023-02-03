# Generated by Django 4.1.6 on 2023-02-03 17:57

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Query",
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
                ("user_name", models.CharField(max_length=100)),
                ("registration_id", models.CharField(max_length=200)),
                ("college_name", models.CharField(max_length=400)),
                ("title", models.CharField(max_length=30)),
                ("description", tinymce.models.HTMLField()),
                ("transaction_id", models.CharField(max_length=500)),
                ("screenshot", models.ImageField(upload_to="references/")),
                ("slug", models.SlugField(blank=True)),
            ],
        ),
    ]
