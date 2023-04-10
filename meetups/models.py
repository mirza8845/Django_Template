from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.name})'

class Participant(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    organizer_email = models.EmailField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'