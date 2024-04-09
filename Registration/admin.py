from django.contrib import admin
from .models import ShelterInformation, Shelter, GeneralUser

# Register your models here.
admin.site.register(ShelterInformation)
admin.site.register(Shelter)
admin.site.register(GeneralUser)