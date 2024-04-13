from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
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

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        user = self.request.user
        if user.is_staff:  #  `is_staff` is used to indicate a Shelter user
            return reverse_lazy('shelter')  
        else:
            return reverse_lazy('pet_feed') 