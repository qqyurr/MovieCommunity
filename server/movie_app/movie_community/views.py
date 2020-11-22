from django.shortcuts import render
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.request
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Review, Review_Comment
from accounts.models import User

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


# user가 작성한 리뷰 리스트 반환 (마이페이지에서 사용)
@api_view(['GET'])
def user_review_list(request):
    my_reviews = request.user.reviews
    serializer = ReviewSerializer(my_reviews, many=True)
    serializer = ReviewSerializer(my_reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# 리뷰작성 & 모든 리뷰 리스트 반환
@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('---------------------------')
            print(request.user.id)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 유저가 리뷰 작성할 때 input에서 영화 제목 검색하면, 밑에 타이틀 쫘르륵 떠서 선택하게 하기
# 혹은 그냥 사이트에서 영화를 검색할 때 사용
@api_view(['GET'])
def search_by_movie_title(request):
    keyword = request.data.get('title')
    searched_movies = Movie.objects.filter(title__contains=keyword)
    serializer = MovieSerializer(searched_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
