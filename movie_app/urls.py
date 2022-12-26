from django.urls import path

from movie_app import views
from movie_app.views import director
from movie_app.views import get_director
from movie_app.views import movie




urlpatterns = [
    path('api/v1/directors/', views.director),
    path('api/v1/directors/<int:pk>/', views.get_director),


    path('api/v1/movies/', views.movie),
    path('api/v1/movies/<int:pk>/', views.get_movie),


    path('api/v1/review/', views.review),
    path('api/v1/review/<int:pk>/', views.get_review),


]