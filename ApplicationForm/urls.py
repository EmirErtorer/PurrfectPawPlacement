from django.urls import path
from . import views

urlpatterns = [
    path('applicationform/', views.test1, name = 'applicationform'),
]