from django.db import models
from django.contrib.auth.models import AbstractUser

# Goverment Database
class ShelterGovernmentRecord(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    
# User
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    # User by default already has username, password and email


# Shelter in Registration Database
class Shelter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# General User in Registration Database
class GeneralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

