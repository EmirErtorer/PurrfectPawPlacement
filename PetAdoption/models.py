from django.db import models
import uuid

class Shelter(models.Model):
    id = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
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
    shelter = models.ForeignKey(Shelter, related_name='pets', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name