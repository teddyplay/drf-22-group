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




# @api_view(['GET'])
# def director(request):
#     query_set = Director.objects.all()
#     data = DirectorSerializer(query_set, many=True).data
#     return Response(data=data)
@api_view(['GET', 'POST'])
def director(request):
    if request.method == "GET":
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializers = DirectorSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        name = request.data.get('name')
        Director.objects.create(
            name=name
        )
        return Response()




# @api_view(["GET"])
# def get_director(request, pk):
#     data = get_object_or_404(Director, pk=pk)
#     serializers = DirectorSerializer(data)
#     return Response(serializers.data)
@api_view(["GET", "PUT", "DELETE"])
def get_director(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = DirectorSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data)






# @api_view(["GET"])
# def movie(request):
#     data = Movie.objects.all()
#     serializer = MovieSerializer(data, many=True)
#
#     if data:
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response(data={"errors"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET', 'POST'])
def movie(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializers = MovieSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response()




# @api_view(["GET"])
# def get_movie(request, pk):
#     data = get_object_or_404(Movie, pk=pk)
#     serializer = MovieSerializer(data)
#     return Response(serializer.data)
@api_view(["GET","PUT","DELETE"])
def get_movie(request, id):
    try:
         movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = ReviewSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        title.save()
        description.save()
        duration.save()
        director_id.save()
        return Response(data=MovieSerializer(movie).data)





# @api_view(["GET"])
# def review(request):
#     review = Review.objects.all()
#     serializer = ReviewSerializer(review, many=True)
#     if review:
#         return Response(serializer.data, status.HTTP_200_OK)
#     else:
#         return Response(data={"Error"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET', 'POST'])
def review(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializers = ReviewSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )
        return Response()



# @api_view(["GET"])
# def get_review(request, pk):
#     data = get_object_or_404(Review, pk=pk)
#     serializer = ReviewSerializer(data)
#     return Response(serializer.data)
@api_view(["GET", "POST", "DELETE"])
def get_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = ReviewSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors':serializers.errors})
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        text.save()
        stars.save()
        movie_id.save()
        return Response(data=ReviewSerializer(review).data)






# class DirectorView(generics.ListAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer
