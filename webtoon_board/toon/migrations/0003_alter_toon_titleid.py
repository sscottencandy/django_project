# Generated by Django 4.1 on 2023-06-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toon", "0002_alter_toon_titleid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="toon",
            name="titleid",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
