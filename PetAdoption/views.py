from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Pet, Shelter

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