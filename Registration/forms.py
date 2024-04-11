from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import ShelterGovernmentRecord, User, GeneralUser, Shelter
from django.core.exceptions import ValidationError

class GeneralUserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=255, required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = False  # Assuming is_staff indicates a non-shelter user
        user.save()
        general_user = GeneralUser.objects.create(user=user)
        general_user.first_name = self.cleaned_data.get('first_name')
        general_user.last_name = self.cleaned_data.get('last_name')
        general_user.save()
        return user

class ShelterSignUpForm(UserCreationForm):
    id = forms.CharField(max_length=11)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address']

    def clean_id(self):
        id = self.cleaned_data['id']
        if not ShelterGovernmentRecord.objects.filter(id=id).exists():
            raise ValidationError("ID does not exist in government records.")
        return id

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True  # Assuming is_staff indicates a shelter user, adjust as needed
        user.save()
        shelter_id = self.cleaned_data.get('id')
        goverment_record = ShelterGovernmentRecord.objects.get(id=shelter_id)
        Shelter.objects.create(
            user=user,
            # Additional logic to copy fields from ShelterGovermentRecord if necessary
        )
        return user