from django.db import models
import datetime

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