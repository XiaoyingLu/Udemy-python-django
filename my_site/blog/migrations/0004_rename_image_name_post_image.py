# Generated by Django 5.0.1 on 2024-01-22 01:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_image_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="image_name",
            new_name="image",
        ),
    ]