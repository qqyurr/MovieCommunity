from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # fields = ('title', 'year')
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'movie', 'star')
