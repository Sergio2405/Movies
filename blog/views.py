#http responses
from django.http import HttpResponse
from django.shortcuts import render, redirect

#.models
from .models import Actor, Director, Movie, Genre

#user model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#django rest framework imports and serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    MovieSerializer, 
    DirectorSerializer, 
    ActorSerializer
)

@login_required(login_url='Login')
def profile(request):
    print(request.user.username)
    return render(request, "blog/profile.html")

@login_required(login_url='Login')
def contact(request):
    return render(request,"blog/contact.html")

def logout_user(request):
    logout(request)

    print("Loggouteado")

    return render(request,"blog/logout.html")

def login_user(request):

    if request.method == "POST":

        user_name = request.POST['user']
        password = request.POST['password']
        print(user_name,password)

        user = authenticate(username = user_name, password=password)
        print(user)

        if user is not None:

            login(request,user)

            print("Usuario loggeado")
            print(user_name,password)

            return render(request, "blog/succesful.html", context = {
                "username": user.username
            })
        
        else:
            return render(request, "blog/login.html", context = {
                "logged" : True
            })
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

        return render(request, "blog/succesful.html")
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
        
        if 'Review Date' in applied_filters:
            new_movie_list.sort(
                key = lambda movie: movie.review_date
            )

        if 'A-Z'in applied_filters:
            new_movie_list.sort(
                key = lambda movie: movie.name
            )

            print("By Alfa",new_movie_list)

        if 'search' in applied_filters:

            movie_searched = request.POST['search']
            print(movie_searched)

            if movie_searched != '':
                final_movie_list = [] 
                movie_searched = movie_searched.lower().split()  
                for movie in new_movie_list:
                    movie_words = movie.name.lower().split(' ')
                    
                    matched = 0
                    for word in movie_words:
                        if (word in movie_searched):
                            matched += 1 

                    if matched >= 1:
                        final_movie_list.append(movie)

                new_movie_list = final_movie_list

        print("New list",new_movie_list)

        return render(request,"blog/movies.html",context={
            "movies_list" :new_movie_list,
            "genres" : Genre.objects.all(),
            "applied_filters" : applied_filters,
            "searched": movie_searched
        })

    else:      

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
                    key = lambda director: director.name
                )

                print("By Alfa",director_list)

        if 'search' in applied_filters:

            director_searched = request.POST['search']
            print(director_searched)

            if director_searched != '':
                final_director_list = [] 
                director_searched = director_searched.lower().split()  
                for director in director_list:
                    director_words = director.name.lower().split(' ')
                    
                    matched = 0
                    for word in director_words:
                        if (word in director_searched):
                            matched += 1 

                    if matched >= 1:
                        final_director_list.append(director)

                director_list = final_director_list
        
        return render(request,"blog/directors.html",context={
            "directors_list" : director_list,
            "applied_filters" : applied_filters,
            "searched": director_searched
        })

    else:

        return render(request,"blog/directors.html",context={
            "directors_list" : director_list
        })

def actors(request):

    actor_list = list(Actor.objects.all())
    
    if request.method == "POST":
        applied_filters = list(request.POST.dict().keys())[1:]
        print(applied_filters)

        if 'A-Z' in applied_filters:
                actor_list.sort(
                    key = lambda actor: actor.name
                )

                print("By Alfa",actor_list)

        if 'search' in applied_filters:

            actor_searched = request.POST['search']
            print(actor_searched)

            if actor_searched != '':
                final_actor_list = [] 
                actor_searched = actor_searched.lower().split()  
                for actor in actor_list:
                    actor_words = actor.name.lower().split(' ')
                    
                    matched = 0
                    for word in actor_words:
                        if (word in actor_searched):
                            matched += 1 

                    if matched >= 1:
                        final_actor_list.append(actor)

                actor_list = final_actor_list
        
        return render(request,"blog/actors.html",context={
            "actors_list" : actor_list,
            "applied_filters" : applied_filters,
            "searched": actor_searched
        })
        
    else:

        return render(request,"blog/actors.html",context={
            "actors_list" : actor_list
        })

def actorsdetail(request,pk):

    actor = Actor.objects.get(id=pk)
    movie_list = list(actor.movies.all())

    if request.method == "POST":
        
        applied_filters = list(request.POST.dict().keys())[1:]
        print(applied_filters)

        if 'Year' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.release_date
                )

                print("By Year",movie_list)
        
        if 'Movie' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.name
                )

                print("By Name",movie_list)

        if 'Our_score' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.final_score
                )

                print("By Our Score",movie_list)
            
        if 'Rotten' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.rotten_tomatoes
                )

                print("By Rotten",movie_list)

        if 'imdb' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.imdb
                )

                print("By Imdb",movie_list)

        movie_list.reverse()

        return render(request,"blog/directorsdetail.html",context={
                "director": actor,
                "movie_list" : movie_list,
                "applied_filters" : applied_filters
            })
    else:
        return render(request,"blog/directorsdetail.html",context={
            "director": actor,
            "movie_list" : movie_list,
        })

def directorsdetail(request,pk):

    director = Director.objects.get(id=pk)
    movie_list = list(director.movie_set.all())

    if request.method == "POST":
        
        applied_filters = list(request.POST.dict().keys())[1:]
        print(applied_filters)

        if 'Year' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.release_date
                )

                print("By Year",movie_list)
        
        if 'Movie' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.name
                )

                print("By Name",movie_list)

        if 'Our_score' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.final_score
                )

                print("By Our Score",movie_list)
            
        if 'Rotten' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.rotten_tomatoes
                )

                print("By Rotten",movie_list)

        if 'imdb' in applied_filters:
                movie_list.sort(
                    key = lambda movie: movie.imdb
                )

                print("By Imdb",movie_list)

        movie_list.reverse()

        return render(request,"blog/directorsdetail.html",context={
                "director": director,
                "movie_list" : movie_list,
                "applied_filters" : applied_filters
            })
    else:
        return render(request,"blog/directorsdetail.html",context={
            "director": director,
            "movie_list" : movie_list,
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

# @api_view(['GET'])
# def director_collection(request):

#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = MovieSerializer(directors,many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def actor_collection(request):

#     if request.method == 'GET':
#         actors = Actor.objects.all()
#         serializer = MovieSerializer(actors,many=True)
#         return Response(serializer.data)