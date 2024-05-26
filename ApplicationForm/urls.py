from django.urls import path
from . import views

app_name = 'applicationform'

urlpatterns = [
    path('apply/<int:pet_id>/', views.apply_for_adoption, name='apply_for_adoption'),
    path('applications/<int:pet_id>/', views.view_applications, name='view_applications'),
]
