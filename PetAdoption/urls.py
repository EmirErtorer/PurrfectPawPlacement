from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_feed, name='pet_feed'),
    path('pet/<str:id>/', views.pet_profile, name='pet_profile'),
    path('shelters/', views.shelter_feed, name='shelter_feed'),
    path('shelters/<str:id>/', views.shelter_detail, name='shelter_detail'),
]
