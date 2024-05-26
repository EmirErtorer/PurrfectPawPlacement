from django.shortcuts import render, redirect, get_object_or_404
from .models import AdoptionApplication
from PetAdoption.models import Pet
from .forms import AdoptionApplicationForm

def apply_for_adoption(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    user = request.user.generaluser
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.pet = pet
            application.applicant = user
            application.save()
            return redirect('pet_profile', id=pet_id)
    else:
        initial_data = {
            'first_name': user.user.first_name,
            'last_name': user.user.last_name,
            'address': user.user.address,
            'phone_number': user.user.phone_number,
            'email': user.user.email,
        }
        form = AdoptionApplicationForm(initial=initial_data)
    return render(request, 'application_form.html', {'form': form, 'pet': pet})

def view_applications(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    applications = pet.applications.all()
    return render(request, 'view_applications.html', {'pet': pet, 'applications': applications})