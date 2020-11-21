from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.request
from bs4 import BeautifulSoup

# Create your views here.


@api_view(['GET'])
def movie_list(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.order_by("id")[:10]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def movie_list(request):
#     # movies = get_list_or_404(Movie)
#     movies = Movie.objects.order_by("id")[:10]

#     for movie in movies:
#         url = 'https://www.imdb.com/title/'
#         movie_id = movie.imdb_title_id
#         url = url + movie_id
#         req = urllib.request.Request(url)
#         res = urllib.request.urlopen(url).read()
#         soup = BeautifulSoup(res, 'html.parser')
#         soup = soup.find("div", class_="poster")
#         imgUrl = soup.find("img")["src"]
#         movie.poster_path = imgUrl
#         movie.save()
#         print('saved')

#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


def get_poster_path(request):
    pass
