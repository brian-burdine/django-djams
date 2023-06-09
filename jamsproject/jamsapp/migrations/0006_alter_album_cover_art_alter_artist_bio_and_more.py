# Generated by Django 4.2 on 2023-04-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamsapp', '0005_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_art',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
