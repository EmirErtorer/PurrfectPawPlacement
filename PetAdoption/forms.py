from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['species', 'name', 'age', 'breed', 'disability', 'pictures', 'allergies', 'availability', 'gender', 'health_status', 'videos']

