from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = "Home"),
    path('movies/', views.MoviesView.as_view(), name = "Movies"),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(),name='MoviesDetail'),
    path('directors/', views.DirectorsView.as_view(),name="Directors"),
    path('directors/<int:pk>', views.DirectorsDetailView.as_view(),name="DirectorsDetail"),
    path('actors/', views.ActorsView.as_view(), name = "Actors"),
    path('actors/<int:pk>/', views.ActorsDetailView.as_view(),name='ActorsDetail'),
]


