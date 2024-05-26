# populate_pets.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PurrfectPawPlacement.settings")
django.setup()

from PetAdoption.models import Pet

# Your code to create Pet instances goes here
dummy_pets = [
    {"species": "Dog", "name": "Buddy", "age": 3, "breed": "Golden Retriever", "disability": "None", "allergies": "None", "availability": True, "gender": "Male", "health_status": "Healthy"},
    {"species": "Cat", "name": "Whiskers", "age": 2, "breed": "Siamese", "disability": "Blind in one eye", "allergies": "None", "availability": True, "gender": "Female", "health_status": "Healthy"},
    {"species": "Dog", "name": "Max", "age": 5, "breed": "Beagle", "disability": "None", "allergies": "Grass", "availability": False, "gender": "Male", "health_status": "Healthy"},
    {"species": "Cat", "name": "Shadow", "age": 4, "breed": "Maine Coon", "disability": "None", "allergies": "None", "availability": True, "gender": "Male", "health_status": "Healthy"},
    {"species": "Dog", "name": "Lucy", "age": 2, "breed": "Poodle", "disability": "Deaf", "allergies": "Beef", "availability": True, "gender": "Female", "health_status": "Healthy"},
    {"species": "Cat", "name": "Bella", "age": 3, "breed": "Persian", "disability": "None", "allergies": "None", "availability": False, "gender": "Female", "health_status": "Healthy"},
    {"species": "Dog", "name": "Rocky", "age": 6, "breed": "German Shepherd", "disability": "Hip dysplasia", "allergies": "None", "availability": True, "gender": "Male", "health_status": "Needs attention"},
    {"species": "Cat", "name": "Simba", "age": 1, "breed": "Bengal", "disability": "None", "allergies": "Chicken", "availability": True, "gender": "Male", "health_status": "Healthy"},
    {"species": "Dog", "name": "Charlie", "age": 4, "breed": "Border Collie", "disability": "None", "allergies": "None", "availability": True, "gender": "Female", "health_status": "Healthy"},
    {"species": "Cat", "name": "Molly", "age": 5, "breed": "British Shorthair", "disability": "None", "allergies": "Fish", "availability": False, "gender": "Female", "health_status": "Healthy"},
]

for pet_info in dummy_pets:
    pet = Pet(**pet_info)
    pet.save()

print("Dummy pet entries created successfully.")
