from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)  # 하나이상부를때는 get_list_or_404
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
