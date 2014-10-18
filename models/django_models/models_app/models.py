from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Musician(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=254)
    release_date = models.DateField()
    num_stars = models.IntegerField()
