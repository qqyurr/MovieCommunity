from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.request
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.


@api_view(['GET'])
def movie_list(request):
    # movies = get_list_or_404(Movie)
    comedy_movies = Movie.objects.filter(genre__startswith="Comedy")[:10]
    romance_movies = Movie.objects.filter(genre__startswith="Romance")[:10]
    thriller_movies = Movie.objects.filter(genre__startswith="Thriller")[:10]
    action_movies = Movie.objects.filter(genre__startswith="Action")[:10]
    horror_movies = Movie.objects.filter(genre__startswith="Horror")[:10]

    comedy_movies_serializer = MovieSerializer(comedy_movies, many=True)
    romance_movies_serializer = MovieSerializer(romance_movies, many=True)
    thriller_movies_serializer = MovieSerializer(thriller_movies, many=True)
    action_movies_serializer = MovieSerializer(action_movies, many=True)
    horror_movies_serializer = MovieSerializer(horror_movies, many=True)

    response_data = {}
    response_data['comedy_movies'] = comedy_movies_serializer.data
    response_data['romance_movies'] = romance_movies_serializer.data
    response_data['thriller_movies'] = thriller_movies_serializer.data
    response_data['action_movies'] = action_movies_serializer.data
    response_data['horror_movies'] = horror_movies_serializer.data

    return JsonResponse(response_data)

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
    movies = get_list_or_404(Movie)
    for movie in movies:
        movie.poster_path = 'https://m.media-amazon.com/images/M/MV5BNmI5ZmM2NDgtMmNjNi00ZjY4LWJmZmYtYWVkNjdhODNiZjdiXkEyXkFqcGdeQXVyMTIxODU0NzI5._V1_UX182_CR0,0,182,268_AL_.jpg'
        movie.save()
    return JsonResponse({'message': 'okay'})
