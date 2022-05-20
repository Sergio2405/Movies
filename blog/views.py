#http responses
from django.http import HttpResponse
from django.shortcuts import render, redirect

#.models
from .models import Actor, Director, Movie, Genre

#user model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#django rest framework imports and serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer


def login_user(request):
    if request.method == "POST":

        user_name = request.POST['user']
        password = request.POST['password']

        user = authenticate(request, username = user_name, password=password)

        if user is not None:
            login(request,user)
        
        else:
            pass

        print(user_name,password)

        return render(request, "blog/succesful.html")
    else:
        return render(request, "blog/login.html")


def register_user(request):

    if request.method == "POST":

        user_name = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']

        print(user_name, email, password)

        user = User.objects.create_user(
            user_name,
            email,
            password
        )

        print(user)

        user.save()

        print("usuario creado")

        return render(request, "blog/register.html")
    else:
        return render(request, "blog/register.html")


def general(request):
    return redirect('Home')

def home(request):
    return render(request,"blog/Home.html")

def movies(request):

    if request.method == "POST":

        applied_filters = list(request.POST.dict().keys())[1:]
        print(applied_filters)
        
        genres_names = list(map(lambda genre: genre.name, Genre.objects.all()))
        genres_post = [genre for genre, id in request.POST.dict().items() if genre in genres_names]
        genres_post.sort()

        movie_list = Movie.objects.all()

        print(genres_post)

        new_movie_list = list(movie_list) if len(genres_post) == 0 else []

        if 'Exact Matching' in applied_filters:
            
            for movie in movie_list: 
                movie_genre = list(map(lambda genre: genre.name , movie.genres.all()))
                movie_genre.sort()

                if movie_genre == genres_post:
                    print(movie.name)
                    new_movie_list.append(movie)
                
        else:

            if len(genres_post) != 0:

                for movie in movie_list: 
                    movie_genre = list(map(lambda genre: genre.name , movie.genres.all()))
                    for genre in genres_post:
                        if genre in movie_genre:
                        
                            new_movie_list.append(movie)
                            break
        
        print("By Genre",new_movie_list)

        if 'Release Date' in applied_filters:
            new_movie_list.sort(
                key = lambda movie: movie.release_date
            )

            print("By Release Date",new_movie_list)
        
        # if 'review_date' in applied_filters:
        #     new_movie_list.sort(
        #         key = lambda movie: movie.review_release_date
        #     )

        if 'A-Z'in applied_filters:
            new_movie_list.sort(
                key = lambda movie: movie.name
            )

            print("By Alfa",new_movie_list)

        print("New list",new_movie_list)

        return render(request,"blog/movies.html",context={
            "movies_list" : new_movie_list,
            "genres" : Genre.objects.all(),
            "applied_filters" : applied_filters
        })
            
    return render(request,"blog/movies.html",context={
        "movies_list" : Movie.objects.all(),
        "genres" : Genre.objects.all()
    })

def directors(request):

    director_list = list(Director.objects.all())
    
    if request.method == "POST":
        applied_filters = list(request.POST.dict().keys())[1:]
        print(applied_filters)

        if 'A-Z'in applied_filters:
                director_list.sort(
                    key = lambda movie: movie.name
                )

                print("By Alfa",director_list)

    return render(request,"blog/directors.html",context={
        "directors_list" : director_list
    })

def actors(request):

    actor_list = list(Actor.objects.all())
    
    if request.method == "POST":
        applied_filters = list(request.POST.dict().keys())[1:]
        print(applied_filters)

        if 'A-Z'in applied_filters:
                actor_list.sort(
                    key = lambda movie: movie.name
                )

                print("By Alfa",actor_list)
    
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

# @api_view(['GET'])
# def movie_collection(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)