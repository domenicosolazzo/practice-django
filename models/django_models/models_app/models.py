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
    id_musician = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=254)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __unicode__(self):              
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Topping(models.Model):
    type = models.CharField(max_length=254)

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
