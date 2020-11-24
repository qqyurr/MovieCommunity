from django.urls import path, include
from . import views


urlpatterns = [
    # GET : 전체 영화 리스트 반환
    path('all_movies/', views.all_movie_list),

    # GET : 장르별 영화 리스트 반환
    path('movie_list_by_genre/', views.movie_list_by_genre),

    # GET : 아이디에 맞는 영화 객체 반환
    path('specific_movie/', views.get_movie_by_id),

    # GET/POST : 특정 영화의 리뷰 리스트, 리뷰 작성
    path('movies/<int:movie_id>/reviews', views.reviewDetail),

    # GET/POST : 전체 리뷰 리스트, 리뷰 작성
    path('reviews/', views.review_list),

    # GET : 로그인한 유저가 작성한 리뷰 리스트
    path('user_reviews/', views.user_review_list),

    # GET/POST : 리뷰에 달린 코멘트 리스트, 리뷰에 코멘트 작성
    path('reviews/comments', views.comment_list),

    # GET : 영화 제목 검색 결과 반환
    path('search_movie_title/', views.search_by_movie_title),

    # GET : 영화 추천 결과 반환
    path('recommend/<str:genre>/', views.recommend_movie),



]
