# Generated by Django 4.1 on 2023-06-16 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("toon", "0005_toon_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="toon", old_name="user", new_name="comment_user",
        ),
    ]
