from django import forms
from .models import Pet

# A form for adding and editing new pets with the specified attributes in the model
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['species', 'name', 'age', 'breed', 'disability', 'pictures', 'allergies', 'availability', 'gender', 'health_status', 'videos']

