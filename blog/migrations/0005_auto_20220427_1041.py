# Generated by Django 3.2.9 on 2022-04-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220427_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote_movie',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='scene_movie',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
    ]
