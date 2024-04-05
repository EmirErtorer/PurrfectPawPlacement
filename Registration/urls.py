from django.urls import path
from . import views

urlpatterns = [
    path('godmode/', views.godmode, name = 'godmode'),
]