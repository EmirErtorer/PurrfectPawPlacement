from django.db import models

# Create your models here.
class Pet(models.Model):
    species = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    disability = models.CharField(max_length=255, blank=True)
    pictures = models.ImageField(upload_to='pets', blank=True, null=True)
    allergies = models.CharField(max_length=255, blank=True)
    availability = models.BooleanField(default=True)
    gender = models.CharField(max_length=50)
    health_status = models.CharField(max_length=100)
    videos = models.FileField(upload_to='pet_videos', blank=True, null=True)