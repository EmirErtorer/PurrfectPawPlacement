from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.http import HttpResponseRedirect , Http404
from .forms import GeneralUserSignUpForm, ShelterSignUpForm
from .models import User, Shelter, GeneralUser

# A view for Signing Up a General User
class GeneralUserSignUpView(CreateView):
    model = User
    form_class = GeneralUserSignUpForm
    template_name = 'general_signup.html' # Rendering the page with visual elements
    success_url = reverse_lazy('login') # Redirect to the login page after a successful sign up

# A view for Signing Up a Shelter User
class ShelterSignUpView(CreateView):
    model = Shelter
    form_class = ShelterSignUpForm
    template_name = 'shelter_signup.html' # Rendering the page with visual elements
    success_url = reverse_lazy('login') # Redirect to the login page after a successful sign up

# A view for Logging In
class CustomLoginView(LoginView):
    template_name = 'login.html' # Rendering the page with visual elements

    # Redirect based on the type of the user
    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
           
            try:
                shelter_id = user.username
                return reverse('shelter_profile', args=[shelter_id])  # Redirect Shelter User to their corresponding Shelter Profile
            except AttributeError:
                raise Http404("Error loading the page")  
        else:
            return reverse('pet_feed')  # Redirect General User to the Pet Feed

    # This method is called when valid form data has been POSTed.
    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())