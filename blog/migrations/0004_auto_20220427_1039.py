# Generated by Django 3.2.9 on 2022-04-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220424_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='reference_description',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='actor',
            name='reference_image',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='director',
            name='reference_description',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='director',
            name='reference_image',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='reference_description',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='reference_image',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='scene_movie',
            name='reference_image',
            field=models.URLField(default=''),
        ),
    ]
