# Generated by Django 5.1.7 on 2025-03-22 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galery", "0002_alter_photo_geom"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="slug",
            field=models.SlugField(default=""),
        ),
        migrations.AddField(
            model_name="photo",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
