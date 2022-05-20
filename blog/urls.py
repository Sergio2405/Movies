from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('movies/', views.movies, name = "Movies"),
    path('movies/<int:pk>/', views.moviesdetail,name='MoviesDetail'),
    path('directors/', views.directors,name="Directors"),
    path('directors/<int:pk>', views.directorsdetail,name="DirectorsDetail"),
    path('actors/', views.actors, name = "Actors"),
    path('actors/<int:pk>/', views.actorsdetail,name='ActorsDetail'),
    path('login/', views.login_user , name = "login"),
    path('register/', views.register_user, name = "register"),
    # path('api/v1/movie', views.movie_collection),
]


