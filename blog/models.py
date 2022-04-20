from django.db import models

# Create your models here.

class Actor(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="actor_image",blank=True)

    def __str__(self):
        return self.name

class Director(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="director_image",blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model): 

    name = models.CharField(max_length=50)
    release_date = models.DateField()
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name="movies")
    duration = models.IntegerField(default=0)
    image = models.ImageField(upload_to="movie_image",blank=True)
    rating_dummy = models.IntegerField(default=0)
    genre = models.IntegerField(default=0)
    
    #score fields 
    cinematography = models.FloatField(default=0)
    acting = models.FloatField(default=0)
    editing = models.FloatField(default=0)
    custom = models.FloatField(default=0)
    music = models.FloatField(default=0)
    screenplay = models.FloatField(default=0)

    #fav 3 quotes 
    quote1 = models.CharField(default="",max_length=100)
    quote2 = models.CharField(default="",max_length=100)
    quote3 = models.CharField(default="",max_length=100)

    #fav scenes images and description
    scene1 = models.ImageField(upload_to="scene_image",blank=True)
    scene2 = models.ImageField(upload_to="scene_image",blank=True)
    scene3 = models.ImageField(upload_to="scene_image",blank=True)

    #other pages score
    rotten_tomatoes = models.FloatField(default=0)
    imdb = models.FloatField(default=0)

    @property
    def rating(self):

        ratings = [
            "NR: Not Rated",
            "G: All Ages Admiteed",
            "PG: Parental Guidance Suggested",
            "PG-13: Parents Strongly Cautioned (+13)",
            "R: Restricted (+17)",
            "NC-17: Adults Only"
        ]

        return ratings[self.rating_dummy]

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
