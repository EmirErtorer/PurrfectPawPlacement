from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def godmode(request):
    return HttpResponse("<h1> I am a god </h1>")
