# Generated by Django 3.2.9 on 2022-04-24 16:00

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='actor_movie',
            name='actor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.actor'),
        ),
        migrations.AlterField(
            model_name='actor_movie',
            name='movie',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.movie'),
        ),
        migrations.AlterField(
            model_name='actor_movie',
            name='physical_aspect',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='actor_movie',
            name='role',
            field=models.CharField(blank=True, choices=[('Leading Actor', 'Leading Actor'), ('Leading Actress', 'Leading Actress'), ('Supporting Actor', 'Supporting Actor'), ('Supporting Actress', 'Supporting Actress')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='actor_movie',
            name='time_in_movie',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='character_movie',
            name='actor',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.actor'),
        ),
        migrations.AlterField(
            model_name='character_movie',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.movie'),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(blank=True, default='Non Genre', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='acting',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='movies', to='blog.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cinematography',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='custom',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='editing',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='blog.Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='music',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.ForeignKey(blank=True, default=blog.models.get_default_rating_result, on_delete=django.db.models.deletion.CASCADE, to='blog.rating'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='review',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rotten_tomatoes',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenplay',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='sinopsis',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='quote_movie',
            name='character',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.character_movie'),
        ),
        migrations.AlterField(
            model_name='quote_movie',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='scene_movie',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.movie'),
        ),
    ]
