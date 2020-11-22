from django.urls import path, include
from . import views

urlpatterns = [
    # GET : 전체 영화 리스트
    path('movies/', views.movie_list),

    # GET/POST : 전체 리뷰 리스트, 리뷰 작성
    path('reviews/', views.review_list),

    # GET : 로그인한 유저가 작성한 리뷰 리스트
    path('user_reviews/', views.user_review_list),

    # GET : 영화 제목 검색 결과 반환
    path('search_movie_title/', views.search_by_movie_title),

    path('get_poster_path/', views.get_poster_path),
]
