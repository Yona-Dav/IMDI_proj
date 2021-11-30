from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.date.today, blank=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='nationality')
    available_in_countries = models.ManyToManyField(Country,default=created_in_country)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    film = models.ManyToManyField(Film)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CommentFilm(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('comment', kwargs={'film_id': self.film.id})


class RatingFilm(models.Model):
    RATINGS = (
        ('*', '*'),
        ('* *', '* *'),
        ('* * *', '* * *'),
        ('* * * *', '* * * *'),
        ('* * * * *', '* * * * *'))
    rating = models.CharField(max_length=100,choices=RATINGS)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('rating', kwargs={'film_id': self.film.id})