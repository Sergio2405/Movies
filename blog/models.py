from typing import List
from unittest.util import unorderable_list_difference
from django.db import models

# Create your models here.

class Actor(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="actor_image",blank=True)

    def movies_order(self):
        pass

    def __str__(self):
        return self.name

class Director(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="director_image",blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    
    name = models.CharField(default="Non Genre",max_length=100)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    
    name = models.CharField(default=0,max_length=100)
    rating_dummy = models.IntegerField(default=0)

    @property
    def rating(self):
        return [
            "NR",
            "G",
            "PG",
            "PG-13",
            "R",
            "NC-17"
        ][self.rating_dummy]

    def __str__(self):
        return self.name

class Scores(models.Model):

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.OneToOneField("Movie", on_delete=models.CASCADE)

    time_in_movie = models.IntegerField(default=0)
    physical_aspect = models.IntegerField(default=0)

    def __str__(self):
        return self.actor.name + ' | ' + self.movie.name


def get_default_rating_result():
    """ get a default value for result status; create new result if not available """
    return Rating.objects.get_or_create(name="not_rated",rating_dummy=1)[0].id

class Movie(models.Model): 

    name = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.IntegerField(default=0)
    image = models.ImageField(upload_to="movie_image",blank=True)
    language = models.CharField(default = "", max_length=40)
    sinopsis = models.TextField(default = "")
    review = models.TextField(default = "")

    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating,on_delete=models.CASCADE,default=get_default_rating_result)

    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor, related_name="movies")

    #score fields 
    cinematography = models.FloatField(default=0)
    acting = models.FloatField(default=0)
    editing = models.FloatField(default=0)
    custom = models.FloatField(default=0)
    music = models.FloatField(default=0)
    screenplay = models.FloatField(default=0)

    #fav scenes images and caption
    scene1 = models.ImageField(upload_to="scene_image",blank=True)
    scene1_caption = models.CharField(default="",max_length=100, blank=True)

    scene2 = models.ImageField(upload_to="scene_image",blank=True)
    scene2_caption = models.CharField(default="",max_length=100, blank=True)

    scene3 = models.ImageField(upload_to="scene_image",blank=True)
    scene3_caption = models.CharField(default="",max_length=100, blank=True)

    #fav 3 quotes 
    quote1 = models.CharField(default="",max_length=100, blank=True)
    quote1_character = models.CharField(default="",max_length=100, blank=True)

    quote2 = models.CharField(default="",max_length=100, blank=True)
    quote2_character = models.CharField(default="",max_length=100, blank=True)

    quote3 = models.CharField(default="",max_length=100, blank=True)
    quote3_character = models.CharField(default="",max_length=100, blank=True)

    #other pages score
    rotten_tomatoes = models.FloatField(default=0)
    imdb = models.FloatField(default=0)

    # Crear metodo que reciba numero de actores (self.actors) y a cada uno
    # un diccionario con sus respectivos seccion:score. Si quiero tener las mejores pelis 
    # de un actor, puedo llamar a movie desde Actor e iterar por el actor que deseo y ya

    def scores_json(self):
        return dict(
            Cinematography = self.cinematography,
            Acting = self.acting,
            Editing = self.editing,
            Custom = self.custom,
            Music = self.music,
            Screenplay = self.screenplay
        )

    def icons_scores_json(self):
        return dict(
            Our = self.final_score,
            RottenTomatoes = self.rotten_tomatoes,
            Imdb = self.imdb,
        )

    @property
    def final_score(self):
        scores_dict = self.scores_json()
        total_fields = len(scores_dict.items())
        sum = 0
        for field , score in scores_dict.items():
            sum += score
        average = sum/total_fields
        return round(average,2)

    @property
    def only_year(self):
        return self.release_date.strftime("%Y")

    def __str__(self):
        return self.name