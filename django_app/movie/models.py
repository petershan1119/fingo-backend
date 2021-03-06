from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField()
    daum_code = models.CharField(max_length=50,
                                 unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField()
    daum_code = models.CharField(max_length=50,
                                    unique=True)

    def __str__(self):
        return self.name


class Nation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    actor = models.ManyToManyField(Actor,
                                   through="MovieActorDetail",
                                   blank=True)
    director = models.ManyToManyField(Director,
                                      blank=True)
    genre = models.ManyToManyField(Genre,
                                   blank=True)
    story = models.TextField()
    img = models.URLField()
    first_run_date = models.DateField(null=True, blank=True)
    score = models.FloatField(default=float(0))
    nation_code = models.ManyToManyField(Nation,
                                         blank=True)
    daum_code = models.CharField(max_length=50,
                                 unique=True)

    def __str__(self):
        return self.title


class MovieActorDetail(models.Model):
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Actor)
    role = models.CharField(max_length=100)


class StillCut(models.Model):
    img = models.URLField()
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.movie.title


class BoxofficeRank(models.Model):
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie)
