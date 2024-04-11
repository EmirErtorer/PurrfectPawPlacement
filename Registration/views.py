from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import GeneralUserSignUpForm, ShelterSignUpForm
from .models import User, Shelter, GeneralUser

class GeneralUserSignUpView(CreateView):
    model = User
    form_class = GeneralUserSignUpForm
    template_name = 'general_signup.html'
    success_url = reverse_lazy('login')

class ShelterSignUpView(CreateView):
    model = Shelter
    form_class = ShelterSignUpForm
    template_name = 'shelter_signup.html'
    success_url = reverse_lazy('login')

