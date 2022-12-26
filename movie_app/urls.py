from django.urls import path

from movie_app import views
from movie_app.views import director
from movie_app.views import get_director
from movie_app.views import movie




urlpatterns = [
    path('api/v1/directors/', views.director),
    path('api/v1/directors/<int:id>/', views.get_director),


    path('api/v1/movies/', views.movie),
    path('api/v1/movies/<int:id>/', views.get_movie),


    path('api/v1/review/', views.review),
    path('api/v1/review/<int:id>/', views.get_review),


]
