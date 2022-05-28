from django.contrib import admin
from .models import (
    Actor, Director, Movie, 
    Rating, Genre, Actor_Movie,
    Character_Movie,Scene_Movie,Quote_Movie,
    Profile
    )

from django.contrib.auth.models import User, Group

# Register your models here.

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Rating)
admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "director","rating","only_year")

@admin.register(Actor_Movie)
class Actor_movieAdmin(admin.ModelAdmin):
    list_display = ("actor", "movie","role")

@admin.register(Scene_Movie)
class SceneAdmin(admin.ModelAdmin):
    list_display = ("description", "movie")

@admin.register(Quote_Movie)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("character", "movie","actor")

@admin.register(Character_Movie)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "actor","movie")

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# Remove: admin.site.register(Profile)