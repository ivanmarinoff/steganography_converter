# Generated by Django 5.0 on 2024-01-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audio_steg", "0002_post_date_post_stegimage_post_stegtext_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
