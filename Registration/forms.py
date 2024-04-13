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
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'address']

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
    government_id = forms.CharField(max_length=11, label="Government Issued ID")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['password1', 'password2']

    def clean_government_id(self):
        government_id = self.cleaned_data['government_id']
        if not ShelterGovernmentRecord.objects.filter(id=government_id).exists():
            raise ValidationError("The provided Government ID does not exist in our records.")
        return government_id

    @transaction.atomic
    def save(self, commit=True):
        government_id = self.cleaned_data.get('government_id')
        government_record = ShelterGovernmentRecord.objects.get(id=government_id)

        user = super().save(commit=False)
        user.username = government_record.id  # Using the government ID as the username.
        user.is_staff = True  # Assuming is_staff indicates a non-shelter user
        # Autofilling user details from the government record.
        user.email = government_record.email
        user.first_name = government_record.name
        user.phone_number = government_record.phoneNumber
        user.address = government_record.address
        user.save()

        # Create the Shelter instance linked to the user.
        Shelter.objects.create(
            user=user,
        )

        return user