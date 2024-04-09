from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Pet, Shelter

def pet_feed(request):
    pet_list = Pet.objects.all() 
    paginator = Paginator(pet_list, 10)  # Show 10 pets per page

    page = request.GET.get('page')  # Get the page number from the request
    try:
        pets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        pets = paginator.page(1)
    except EmptyPage:
        pets = paginator.page(paginator.num_pages)

    return render(request, 'PetAdoption/pet_feed.html', {'pets': pets})

def shelter_feed(request):
    shelters = Shelter.objects.all()
    return render(request, 'PetAdoption/shelter_feed.html', {'shelters': shelters})

def pet_profile(request, id):
    pet = Pet.objects.get(id=id)
    return render(request, 'PetAdoption/pet_profile.html', {'pet': pet})
