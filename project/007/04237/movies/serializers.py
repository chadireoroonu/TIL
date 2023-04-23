from rest_framework import serializers
from .models import Movie, Actor, Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        field = '__all__'