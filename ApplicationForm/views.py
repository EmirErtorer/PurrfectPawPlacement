from django.shortcuts import render, redirect, get_object_or_404
from .models import AdoptionApplication
from PetAdoption.models import Pet
from .forms import AdoptionApplicationForm
from django.contrib import messages 

def apply_for_adoption(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    user = request.user.generaluser

    # Check if the user has already applied for this pet
    existing_application = AdoptionApplication.objects.filter(pet=pet, applicant=user).exists()
    
    if existing_application:
        messages.error(request, "You have already applied to adopt this pet.")
        return redirect('pet_profile', id=pet_id)

    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.pet = pet
            application.applicant = user
            application.save()
            messages.success(request, "Your application has been submitted.")
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