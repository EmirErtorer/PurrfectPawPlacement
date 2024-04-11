from django.contrib import admin
from .models import ShelterGovernmentRecord, User, GeneralUser, Shelter

# Register your models here.
admin.site.register(ShelterGovernmentRecord)
admin.site.register(User)
admin.site.register(GeneralUser)
admin.site.register(Shelter)
