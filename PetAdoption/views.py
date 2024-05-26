from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse # For redirection to specified URLs
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # To paginate pages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # For security
from django.views.generic import UpdateView, DeleteView 
from django.contrib.auth import get_user_model
from .models import Pet, Shelter
from .forms import PetForm
from ApplicationForm.models import AdoptionApplication


User = get_user_model() # Fetching the current user details

# A view for browsing by Pet Feed
def pet_feed(request):
    pet_list = Pet.objects.all() # Getting all the pet objects from the Pet Model
    pet_list = filter_pets(pet_list, request) # Filtering the pets based on user choice

    breeds_list = Pet.objects.values_list('breed', flat=True).distinct().order_by('breed') # Breed filter
    species_list = Pet.objects.values_list('species', flat=True).distinct() # Species filter

    pets = paginate_queryset(request, pet_list, 10) # Displaying a total of 10 pets for each page
 
    # Rendering the page with visual elements
    return render(request, 'PetAdoption/pet_feed.html', {
        'pets': pets,
        'species_list': species_list,
        'breeds_list': breeds_list,
    })

# A view for accessing each Pet Profile
def pet_profile(request, id):
    pet = get_object_or_404(Pet, id=id)
    user = request.user.generaluser
    existing_application = AdoptionApplication.objects.filter(pet=pet, applicant=user).exists()
    return render(request, 'PetAdoption/pet_profile.html', {'pet': pet, 'existing_application': existing_application})


# A view for browsing by Shelter Feed
def shelter_feed(request):
    shelters = Shelter.objects.all() # Getting all the shelter objects from the Shelter Model
    shelters = paginate_queryset(request, shelters, 10)

    # Rendering the page with visual elements
    return render(request, 'PetAdoption/shelter_feed.html', {'shelters': shelters})

# A view for browsing the available pets for a specific Shelter
def shelter_detail(request, id):
    shelter = Shelter.objects.get(id=id) # Getting all the shelter objects from the Shelter Model
    pet_list = shelter.pets.all()  # Getting all the pet objects from a specific shelter
    pet_list = filter_pets(pet_list, request) # Filtering the pets based on user choice

    breeds_list = Pet.objects.values_list('breed', flat=True).distinct().order_by('breed') # Breed filter
    species_list = Pet.objects.values_list('species', flat=True).distinct() # Species filter

    pets = paginate_queryset(request, pet_list, 10) # Displaying a total of 10 shelters for each page

    # Rendering the page with visual elements
    return render(request, 'PetAdoption/shelter_detail.html', {
        'shelter': shelter,
        'pets': pet_list,
        'breeds_list': breeds_list,
        'species_list': species_list
    })

# A view for Shelter Profiles for each Shelter User
@login_required # Prevents non-logged-in Users from accessing the corresponding URL
def shelter_profile(request, id):
    # Check if the user is a shelter user
    if not request.user.is_staff:
        raise Http404("You are not registered as a shelter.")

    # Fetch the shelter or return 404 if there is an error
    shelter = get_object_or_404(Shelter, id=id)

    pet_list = Pet.objects.filter(shelter=shelter) # Getting all the pet objects from a specific shelter
    pets = paginate_queryset(request, pet_list, 10) # Displaying a total of 10 shelters for each page

    # Handling POST request for adding new pet
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES) # Submit the filled in form for adding a new pet
        if form.is_valid():
            pet = form.save(commit=False)
            pet.shelter = shelter # Specify the newly added pet's corresponding shelter
            pet.save() # Save the newly added pet into the Pet table
            return HttpResponseRedirect(request.path_info)
    else:
        form = PetForm() # Provide the form

    # Rendering the page with visual elements
    return render(request, 'PetAdoption/shelter_profile.html', {
        'shelter': shelter,
        'pets': pets,
        'form': form
    })

# A view for updating an existing pet's information
class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm  # Updates will be done through a form
    template_name = 'PetAdoption/pet_edit.html' # Rendering the page with visual elements

    # A function that returns the requested pet after a security check
    def get_object(self, queryset=None):
        pet = super().get_object(queryset) # To ensure the pet belongs to the logged-in shelter
        return pet

    # A function for getting the pets available in that specific shelter
    def get_queryset(self):
        if self.request.user.is_staff: # To ensure that the logged in user is a Shelter User
            shelter_id = self.kwargs.get('shelter_id') # Get the shelter id of the currently logged in user
            shelter = get_object_or_404(Shelter, id=shelter_id) # Get the specific shelter with the shelter_id or raise error
            return Pet.objects.filter(shelter=shelter) # Return the pets available in that specific shelter
        return Pet.objects.none()  # Returns an empty queryset for non-shelter users

    # A function to redirect back to the shelter profile page after an update to the pet information
    def get_success_url(self):
        return reverse('shelter_profile', kwargs={'id': self.kwargs['shelter_id']}) # Redirect to the shelter's profile page
    
# A view for deleting an existing pet
class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'PetAdoption/pet_confirm_delete.html' # Rendering the page with visual elements

    # A function that returns the requested pet after a security check
    def get_object(self, queryset=None):
        pet = super().get_object(queryset) # To ensure the pet belongs to the logged-in shelter
        return pet

    # A function for getting the pets available in that specific shelter
    def get_queryset(self):
        if self.request.user.is_staff: # To ensure that the logged in user is a Shelter User
            shelter_id = self.kwargs.get('shelter_id') # Get the shelter id of the currently logged in user
            shelter = get_object_or_404(Shelter, id=shelter_id) # Get the specific shelter with the shelter_id or raise error
            return Pet.objects.filter(shelter=shelter)# Return the pets available in that specific shelter
        return Pet.objects.none()  # Returns an empty queryset for non-shelter users

    # A function to redirect back to the shelter profile page after an update to the pet information
    def get_success_url(self):
        return reverse('shelter_profile', kwargs={'id': self.kwargs['shelter_id']}) # Redirect to the shelter's profile page
    
    # A function to pass additonal data to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shelter_id'] = self.kwargs.get('shelter_id')
        return context

    # A function to delete a specified pet
    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff: # To ensure that the logged in user is a Shelter User
            return HttpResponseRedirect(reverse('shelter_profile', kwargs={'id': self.kwargs['shelter_id']}))  # Redirect to the shelter's profile page
        return super(PetDeleteView, self).delete(request, *args, **kwargs) # Delete the specific pet from the Pet Model
    

# A view to filter the available pets
def filter_pets(queryset, request):
    # Filteration for species
    species = request.GET.get('species')
    if species:
        queryset = queryset.filter(species__icontains=species)

    # Filteration for age
    age = request.GET.get('age')
    if age:
        queryset = queryset.filter(age=age)

    # Filteration for breed
    breed = request.GET.get('breed')
    if breed:
        queryset = queryset.filter(breed__icontains=breed)

    # Filteration for gender
    gender = request.GET.get('gender')
    if gender:
        queryset = queryset.filter(gender__iexact=gender)

    # Filteration for allergies
    allergies = request.GET.get('allergies')
    if allergies:
        queryset = queryset.filter(allergies__icontains=allergies)

    return queryset # Return the pets that match the specified filters


# A view to paginate a page 
def paginate_queryset(request, queryset, items_per_page=10):
    paginator = Paginator(queryset, items_per_page)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1) 
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj