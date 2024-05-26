from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_feed, name='pet_feed'), # Initial URL that redirects to pet feed upon login (General User side)
    path('pet/<str:id>/', views.pet_profile, name='pet_profile'), # URL for each pet profile (General User side)
    path('shelters/', views.shelter_feed, name='shelter_feed'), # URL for browsing by shelters (General User side)
    path('shelters/<str:id>/', views.shelter_detail, name='shelter_detail'), # URL for specific shelter profiles (General User side)
    path('shelter_profile/<str:id>/', views.shelter_profile, name='shelter_profile'), # URL for specific shelter profiles (Shelter User side)
    path('shelter/<str:shelter_id>/pet/<str:pk>/edit/', views.PetUpdateView.as_view(), name='edit_pet'), # URL for editing a specific pet (Shelter User side)
    path('shelter/<str:shelter_id>/pet/<str:pk>/delete/', views.PetDeleteView.as_view(), name='delete_pet'), # URL for deleting a specific pet (SHelter User side)
]

