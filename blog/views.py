from django.views.generic import (
    ListView, 
    DetailView,
    TemplateView
)
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Actor, Director, Movie

class HomeView(TemplateView):
    template_name = "blog/Home.html"

class MoviesView(ListView):

    model = Movie 
    template_name = "blog/movies.html"
    queryset = Movie.objects.all()
    context_object_name = "movies_list"

class MovieDetailView(DetailView):

    model = Movie 
    template_name = "blog/moviesdetail.html"

class DirectorsView(ListView):

    model = Director
    template_name = "blog/directors.html"
    queryset = Director.objects.all()
    context_object_name = "directors_list"

class DirectorsDetailView(DetailView):

    model = Director
    template_name = "blog/directorsdetail.html"

class ActorsView(ListView):

    model = Actor
    template_name = "blog/actors.html"
    queryset = Actor.objects.all()
    context_object_name = "actors_list"

class ActorsDetailView(DetailView):

    model = Actor
    template_name = "blog/actorsdetail.html"