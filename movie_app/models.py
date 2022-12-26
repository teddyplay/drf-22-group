from django.db import models




class Director(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="Имя и фамилия режиссера",
                            )

    @property
    def movie_count(self):
        return self.movie_set.all().count()


    def __str__(self):
        return self.name




class Movie(models.Model):
    title = models.CharField(max_length=30,
                             verbose_name="Название фильма",
                             )
    description = models.TextField(verbose_name="Описание",
                                   )
    duration = models.IntegerField(default=0,
                                   verbose_name="Продолжительность",
                                   )
    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 verbose_name="Имя режиссера")


    def __str__(self):
        return self.title


    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount





class Review(models.Model):
    text = models.TextField(verbose_name="Отзыв",
                            max_length=500,
                            )
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              )
    stars = models.IntegerField(default=0,
                                max_length=5,
                                verbose_name="Звёзды",
                                )


    def __str__(self):
        return str(self.movie)




