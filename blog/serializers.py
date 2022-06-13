from rest_framework import serializers
from .models import Actor, Director, Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('name','release_date','duration','language',"image")

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields =  ('name','image')

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name','image')