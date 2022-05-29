# models built in
from django.contrib.auth.models import User
from django.db import models

#django utils
from django.db.models.signals import post_save
from django.dispatch import receiver

#python std
import datetime

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = models.ForeignKey("Genre", on_delete=models.CASCADE, blank=True)
    actors = models.ForeignKey("Actor", on_delete=models.CASCADE, blank=True)
    directors = models.ForeignKey("Director", on_delete=models.CASCADE, blank=True)
    movies = models.ForeignKey("Movie", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username

class Actor(models.Model):

    name = models.CharField(max_length=50,blank=True)
    review = models.TextField(default = "",blank=True)
    image = models.ImageField(upload_to='actor_image',blank=True,default="",null=True)
    reference_image = models.URLField(max_length=200, default = "")
    reference_description = models.URLField(max_length=200, default = "")
 
    def __str__(self):
        return self.name

class Director(models.Model):

    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to="director_image",blank=True)
    review = models.TextField(default = "",blank=True)
    reference_image = models.URLField(max_length=200, default = "")
    reference_description = models.URLField(max_length=200, default = "")

    def __str__(self):
        return self.name

class Genre(models.Model):
    
    name = models.CharField(default="Non Genre",max_length=100,blank=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    
    name = models.CharField(default=0,max_length=100,blank=True)

    @property
    def rating(self):
        return {
            "NR" : "Not Rated",
            "G" : "General Audiences",
            "PG" : "Parental Guidance Suggested",
            "PG-13" : "Parents Strongly Cautioned",
            "R" : "Restricted",
            "NC-17" : "Adults Only"
        }[self.name]

    def __str__(self):
        return self.name

class Actor_Movie(models.Model):
    
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE,blank=True) 
    movie = models.OneToOneField("Movie", on_delete=models.CASCADE,blank=True)
    
    role = models.CharField(max_length=50,default = "",choices=[
        ("Leading Actor","Leading Actor"),
        ("Leading Actress","Leading Actress"),
        ("Supporting Actor","Supporting Actor"),
        ("Supporting Actress","Supporting Actress")
    ],blank=True)

    time_in_movie = models.IntegerField(default=0,blank=True)
    physical_aspect = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return '|'.join([self.actor.name,self.movie.name,self.role]) 

class Character_Movie(models.Model):

    name = models.CharField(max_length=50,blank=True,default = "")
    actor = models.OneToOneField(Actor,on_delete=models.CASCADE,blank=True)
    movie = models.ForeignKey("Movie",on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name

class Scene_Movie(models.Model):

    image = models.ImageField(upload_to = "scenes_images",blank=True)
    description = models.CharField(max_length=100,blank=True,default = "")
    movie = models.ForeignKey("Movie",on_delete=models.CASCADE,blank=True)
    caption = models.TextField(default = "",blank=True)

    reference_image = models.URLField(max_length=200, default = "")

    def __str__(self):
        return '|'.join([self.description,self.movie.name]) 

class Quote_Movie(models.Model):

    quote = models.CharField(max_length=100,default = "", blank=True)
    movie = models.ForeignKey("Movie",on_delete=models.CASCADE,blank=True)
    character = models.OneToOneField(Character_Movie,on_delete=models.CASCADE,blank=True)
    description = models.TextField(default = "",blank=True)

    @property
    def actor(self):
        return self.character.actor.name

    def __str__(self):
        return '|'.join([self.character.name,self.movie.name])

def get_default_rating_result():
    """ get a default value for result status; create new result if not available """
    return Rating.objects.get_or_create(name="not_rated")[0].id

class Movie(models.Model): 

    name = models.CharField(max_length=50,blank=True)
    release_date = models.DateField(blank=True)
    duration = models.IntegerField(default=0,blank=True)
    image = models.ImageField(upload_to="movie_image",blank=True,default = "actor_image/ProfilePic.png")
    language = models.CharField(default = "", max_length=40,blank=True)
    sinopsis = models.TextField(default = "",blank=True)
    review = models.TextField(default = "",blank=True)
    review_date = models.DateField(blank=True, default = datetime.date.today)
    

    reference_image = models.URLField(max_length=200, default = "")
    reference_description = models.URLField(max_length=200, default = "")

    director = models.ForeignKey(Director,on_delete=models.CASCADE,blank=True)
    rating = models.ForeignKey(Rating,on_delete=models.CASCADE,default=get_default_rating_result,blank=True)

    genres = models.ManyToManyField(Genre,blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies",blank=True)

    #score fields 
    cinematography = models.FloatField(default=0,blank=True)
    acting = models.FloatField(default=0,blank=True)
    editing = models.FloatField(default=0,blank=True)
    custom = models.FloatField(default=0,blank=True)
    music = models.FloatField(default=0,blank=True)
    screenplay = models.FloatField(default=0,blank=True)

    #other pages score
    rotten_tomatoes = models.FloatField(default=0,blank=True)
    imdb = models.FloatField(default=0,blank=True)

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