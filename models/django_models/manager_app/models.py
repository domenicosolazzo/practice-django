from django.db import models

# Custom managers
class PeopleManager(models.Manager):
    def get_queryset(self):
        return super(PeopleManager, self).get_queryset().filter(first_name__startswith='Domenico')

class PersonQuerySet(models.QuerySet):
    def small_people(self):
        return self.filter(shirt_size='S')

    def medium_people(self):
        return self.filter(shirt_size='M')

class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def small_people(self):
        return self.get_queryset().small_people()

    def medium_people(self):
        return self.get_queryset().medium_people()

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
    people = PersonManager() # Person.people.all()
    people_qs = PersonQuerySet.as_manager() #Person.people_qs.all()
    domenicos = PeopleManager() # Person.domenicos.all()
