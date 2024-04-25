from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_feed, name='pet_feed'),
    path('pet/<str:id>/', views.pet_profile, name='pet_profile'),
    path('shelters/', views.shelter_feed, name='shelter_feed'),
    path('shelters/<str:id>/', views.shelter_detail, name='shelter_detail'),
    path('shelter_profile/<str:id>/', views.shelter_profile, name='shelter_profile'),
    path('shelter/<str:shelter_id>/pet/<str:pk>/edit/', views.PetUpdateView.as_view(), name='edit_pet'),
    path('shelter/<str:shelter_id>/pet/<str:pk>/delete/', views.PetDeleteView.as_view(), name='delete_pet'),
]

