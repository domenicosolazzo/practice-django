from django.db import models

# Custom managers
class PeopleManager(models.Manager):
    def get_queryset(self):
        return super(PeopleManager, self).get_queryset().filter(first_name__startswith='Domenico')


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    # Custom managers
    people = models.Manager() # Person.people.all()
    domenicos = PeopleManager() # Person.domenicos.all()
