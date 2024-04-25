from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.http import HttpResponseRedirect , Http404
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
        if user.is_staff:
           
            try:
                shelter_id = user.username
                return reverse('shelter_profile', args=[shelter_id]) 
            except AttributeError:
                raise Http404("Error loading the page")  
        else:
            return reverse('pet_feed')  # Redirect general users to the general feed

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())