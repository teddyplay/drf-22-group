from rest_framework import serializers
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review





class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3,
                                 max_length=20,
                                 )

    class Meta:
        model = Director
        fields = ['name',
                  'movie_count',
                  ]




class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=200,
                                 min_length=10,
                                 )
    movie_id = serializers.CharField()
    stars = serializers.IntegerField(min_value=1,
                                     max_value=5,
                                     )



    class Meta:
        model = Review
        fields = ["id",
                  "movie_id",
                  "text",
                  "stars",
                  ]




class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    title = serializers.CharField(min_length=2,
                                  max_length=20,
                                  )
    description = serializers.CharField(max_length=400,
                                        min_length=5,
                                        )
    duration = serializers.CharField()
    director_id = serializers.CharField()
    # stars_id = serializers.IntegerField()


    class Meta:
        model = Movie
        fields = ['duration',
                  'id',
                  'director_id',
                  'title',
                  'description',
                  'reviews',
                  'rating',
                  ]






