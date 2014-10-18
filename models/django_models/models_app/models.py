from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)

class Musician(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=254)
    release_date = models.DateField()
    num_stars = models.IntegerField()
