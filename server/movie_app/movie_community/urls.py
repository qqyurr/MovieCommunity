from django.urls import path, include
from . import views

urlpatterns = [
    # movie list 요청 주소
    path('movies/', views.movie_list),
]
