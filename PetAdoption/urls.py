from django.urls import path
from . import views

urlpatterns = [
    path('test1/', views.test1, name = 'test1'),
]