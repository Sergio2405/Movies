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
    path('login/', views.login_user , name = "Login"),
    path('logout/', views.logout_user , name = "Logout"),
    path('register/', views.register_user, name = "Register"),
    path('contact/', views.contact, name = "Contact"),
    path('profile/', views.profile, name = "Profile"),
    # path('api/v1/movie', views.movie_collection),
    # path('api/v1/director', views.director_collection),
    # path('api/v1/actor', views.actor_collection),
]


