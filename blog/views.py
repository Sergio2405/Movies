from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Actor, Director, Movie

def general(request):
    return redirect('Home')

def home(request):
    return render(request,"blog/Home.html")

def movies(request):

    movie_list = Movie.objects.all()
    return render(request,"blog/movies.html",context={
        "movies_list" : movie_list
    })

def directors(request):
    
    director_list = Director.objects.all()
    return render(request,"blog/directors.html",context={
        "directors_list" : director_list
    })

def actors(request):
    
    actor_list = Actor.objects.all()
    return render(request,"blog/actors.html",context={
        "actors_list" : actor_list
    })

def actorsdetail(request,pk):

    actor = Actor.objects.get(id=pk)

    return render(request,"blog/actorsdetail.html",context={
        "actor" : actor
    })

def directorsdetail(request,pk):

    director = Director.objects.get(id=pk)
    
    return render(request,"blog/directorsdetail.html",context={
        "director" : director
    })

def moviesdetail(request,pk):

    movie_0 = Movie.objects.get(id=pk)
  
    genre_dict = {}
    for genre in movie_0.genres.all():
        
        genre_movie_list = list(filter(lambda movie: movie != movie_0, genre.movie_set.all()))
        if len(genre_movie_list) != 0:
            genre_dict[genre.name] = genre_movie_list

    return render(request,"blog/moviesdetail.html",context={
        "movie" : movie_0,
        "genre_dict" : genre_dict
    })