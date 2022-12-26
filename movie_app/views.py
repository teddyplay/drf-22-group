from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from movie_app.serializers import DirectorSerializer
from movie_app.serializers import MovieSerializer
from movie_app.serializers import ReviewSerializer




@api_view(['GET'])
def director(request):
    query_set = Director.objects.all()
    data = DirectorSerializer(query_set, many=True).data
    return Response(data=data)



@api_view(["GET"])
def get_director(request, pk):
    data = get_object_or_404(Director, pk=pk)
    serializers = DirectorSerializer(data)
    return Response(serializers.data)





@api_view(["GET"])
def movie(request):
    data = Movie.objects.all()
    serializer = MovieSerializer(data, many=True)

    if data:
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(data={"errors"}, status=status.HTTP_404_NOT_FOUND)




@api_view(["GET"])
def get_movie(request, pk):
    data = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(data)
    return Response(serializer.data)





@api_view(["GET"])
def review(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    if review:
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        return Response(data={"Error"}, status=status.HTTP_404_NOT_FOUND)




@api_view(["GET"])
def get_review(request, pk):
    data = get_object_or_404(Review, pk=pk)
    serializer = ReviewSerializer(data)
    return Response(serializer.data)





























# class DirectorView(generics.ListAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer


