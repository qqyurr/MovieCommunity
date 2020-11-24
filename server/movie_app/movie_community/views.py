from .serializers import MovieSerializer, ReviewSerializer, ReviewCommentSerializer
from .models import Movie, Review, Review_Comment
from accounts.models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http import JsonResponse, HttpResponse
import json
import urllib.request
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.


@api_view(['GET'])
def all_movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


# 장르별로 10개씩 영화 반환
@api_view(['GET'])
def movie_list_by_genre(request):
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

    return JsonResponse({'movies_by_genre': response_data})


# 아이디로 특정 영화 정보와 그에 달린 리뷰 리스트와 각 리뷰에 달린 코멘트 리스트 반환
@api_view(['GET'])
def get_movie_by_id(request):
    movie_id = request.data.get('movieId')

    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie_id=movie_id)

    for review in reviews:
        comments = Review_Comment.objects.filter(review_id=review.id)
        review.comments = comments

    movie.reviews = reviews

    # movie = Movie.objects.filter(pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def reviewDetail(request, movie_id):
    # GET 요청) 영화정보와 리뷰와 리뷰코멘트들을 묶어 반환.

    print('------------------------------------------------')
    print(movie_id)
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_id)
        reviews = Review.objects.filter(movie_id=movie_id)
        for review in reviews:
            comments = Review_Comment.objects.filter(review_id=review.id)
            review.comments = comments
        movie.reviews = reviews
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # POST 요청)유저가 리뷰를 작성할 때 :
    elif request.method == 'POST':
        content = request.data.get('content')
        star = request.data.get('star')
        movie = get_object_or_404(Movie, pk=movie_id)
        review = Review(content=content, star=star,
                        movie=movie, user=request.user)
        review.save()
        serialized_obj = serializers.serialize('json', [review])

        dict_obj = model_to_dict(review)
        serialized = json.dumps(dict_obj)
        return Response(serialized)

# @api_view(['GET'])
# def movie_list(request):
#     # movies = get_list_or_404(Movie)
#     movies = Movie.objects.order_by("id")[100:]

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
#         print(movie.id)
#     print('completed')
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


# user가 작성한 리뷰 리스트 반환 (마이페이지에서 사용)
@api_view(['GET'])
def user_review_list(request):
    print('------------------------------------------------------------')
    print(request.user.id)
    my_reviews = request.user.reviews
    serializer = ReviewSerializer(
        my_reviews, many=True)
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


# GET/POST : 리뷰에 달린 코멘트 리스트, 리뷰에 코멘트 작성
@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'POST':
        serializer = ReviewCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            # 그냥 아이디만 request body 에 넣어주면  serializer(data=request.data) 로 넣어주면 알아서 해당 아이디의 객체를 찾아서 넣어주는듯..대박 굳이
            # 첨에는 request.POST.get('review') 해서 리뷰 아이디 찾아서 review = Review.objects.filter(id=review_id) 해서 찾아줘서 serializer(review=review)
            # 이렇게 넣어주려고했는데 에러만 나고(user는 User 인스턴스여야 한다는 에러남. querydict 로 와서그런가.) 그냥 아무것도안하면 알아서 장고에서 다 해주는것이었다 디박
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def recommend_movie(request, genre):

    recommend_movies = Movie.objects.filter(
        genre__startswith=genre).order_by('-avg_vote')[:5]
    serializer = MovieSerializer(recommend_movies, many=True)
    return Response(serializer.data)
