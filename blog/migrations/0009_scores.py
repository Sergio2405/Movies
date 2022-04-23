# Generated by Django 3.2.9 on 2022-04-22 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220421_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in_movie', models.IntegerField(default=0)),
                ('physical_aspect', models.IntegerField(default=0)),
                ('actor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.actor')),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.movie')),
            ],
        ),
    ]