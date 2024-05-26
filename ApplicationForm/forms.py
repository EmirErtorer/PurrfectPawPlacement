# applicationform/forms.py
from django import forms
from .models import AdoptionApplication

class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email', 'number_of_children',
                'number_of_pets', 'residence_type', 'income_range', 'activity_level', 'time_availability',
                'prior_pet_experience', 'additional_notes']