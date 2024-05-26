# applicationform/models.py
from django.db import models
from Registration.models import GeneralUser
from PetAdoption.models import Pet

class AdoptionApplication(models.Model):
    # Existing fields
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(GeneralUser, on_delete=models.CASCADE, related_name='applications')
    # New personal information fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    # Remaining fields
    number_of_children = models.IntegerField(default=0)
    number_of_pets = models.IntegerField(default=0)
    residence_type = models.CharField(max_length=100)
    income_range = models.CharField(max_length=100)
    activity_level = models.CharField(max_length=100)
    time_availability = models.CharField(max_length=100)
    prior_pet_experience = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s application for {self.pet.name}"
