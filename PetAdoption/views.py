from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Pet, Shelter
from .forms import PetForm

User = get_user_model()

def pet_feed(request):
    pet_list = Pet.objects.all() 
    pet_list = filter_pets(pet_list, request)

    breeds_list = Pet.objects.values_list('breed', flat=True).distinct().order_by('breed')
    species_list = Pet.objects.values_list('species', flat=True).distinct()

    pets = paginate_queryset(request, pet_list, 10)
 
    return render(request, 'PetAdoption/pet_feed.html', {
        'pets': pets,
        'species_list': species_list,
        'breeds_list': breeds_list,
    })

def pet_profile(request, id):
    pet = Pet.objects.get(id=id)
    return render(request, 'PetAdoption/pet_profile.html', {'pet': pet})


def shelter_feed(request):
    shelters = Shelter.objects.all()
    paginator = Paginator(shelters, 10)  # Show 10 pets per page

    pets = paginate_queryset(request, shelters, 10)

    return render(request, 'PetAdoption/shelter_feed.html', {'shelters': shelters})

def shelter_detail(request, id):
    shelter = Shelter.objects.get(id=id)
    pet_list = shelter.pets.all()  
    pet_list = filter_pets(pet_list, request)

    breeds_list = Pet.objects.values_list('breed', flat=True).distinct().order_by('breed')
    species_list = Pet.objects.values_list('species', flat=True).distinct()

    pets = paginate_queryset(request, pet_list, 10)

    return render(request, 'PetAdoption/shelter_detail.html', {
        'shelter': shelter,
        'pets': pet_list,
        'breeds_list': breeds_list,
        'species_list': species_list
    })


@login_required
def shelter_profile(request, id):
    # Check if the user is a shelter user
    if not request.user.is_staff:
        raise Http404("You are not registered as a shelter.")

    # Fetch the shelter or return 404
    shelter = get_object_or_404(Shelter, id=id)

    # Fetch pets related to the shelter and apply pagination
    pet_list = Pet.objects.filter(shelter=shelter)
    pets = paginate_queryset(request, pet_list, 10)

    # Handling POST request for adding new pet
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.shelter = shelter
            pet.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PetForm()

    return render(request, 'PetAdoption/shelter_profile.html', {
        'shelter': shelter,
        'pets': pets,
        'form': form
    })


class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'PetAdoption/pet_edit.html'

    def get_object(self, queryset=None):
        # This method ensures the pet belongs to the logged-in shelter
        pet = super().get_object(queryset)
        return pet

    def get_queryset(self):
        # Ensures only pets related to the logged-in shelter user are accessible
        if self.request.user.is_staff:
            shelter_id = self.kwargs.get('shelter_id')
            shelter = get_object_or_404(Shelter, id=shelter_id)
            return Pet.objects.filter(shelter=shelter)
        return Pet.objects.none()  # Returns an empty queryset for non-shelter users

    def get_success_url(self):
        # Redirects back to the shelter profile page after the update
        return reverse('shelter_profile', kwargs={'id': self.kwargs['shelter_id']})
    

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'PetAdoption/pet_confirm_delete.html'

    def get_object(self, queryset=None):
        # This method ensures the pet belongs to the logged-in shelter
        pet = super().get_object(queryset)
        return pet

    def get_queryset(self):
        # Ensures only pets related to the logged-in shelter user are accessible
        if self.request.user.is_staff:
            shelter_id = self.kwargs.get('shelter_id')
            shelter = get_object_or_404(Shelter, id=shelter_id)
            return Pet.objects.filter(shelter=shelter)
        return Pet.objects.none()  # Returns an empty queryset for non-shelter users

    def get_success_url(self):
        # Dynamic success URL to redirect to the shelter's profile
        return reverse('shelter_profile', kwargs={'id': self.kwargs['shelter_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shelter_id'] = self.kwargs.get('shelter_id')
        return context

    def delete(self, request, *args, **kwargs):
        """Ensure that delete action checks for the proper user permissions."""
        if not request.user.is_staff:
            return HttpResponseRedirect(reverse('shelter_profile', kwargs={'id': self.kwargs['shelter_id']}))  
        return super(PetDeleteView, self).delete(request, *args, **kwargs)
    

# Filteration function
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

    return queryset


# Pagination function
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