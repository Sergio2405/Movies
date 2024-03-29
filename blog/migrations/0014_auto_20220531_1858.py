# Generated by Django 3.2.9 on 2022-05-31 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='actors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.actor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='directors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.director'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genres',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.genre'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='movies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.movie'),
        ),
    ]
