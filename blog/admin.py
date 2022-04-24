from django.contrib import admin
from .models import (
    Actor, Director, Movie, 
    Rating, Genre, Actor_Movie,
    Character_Movie,Scene_Movie,Quote_Movie
    )
# Register your models here.

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Actor_Movie)
admin.site.register(Character_Movie)
admin.site.register(Scene_Movie)
admin.site.register(Quote_Movie)