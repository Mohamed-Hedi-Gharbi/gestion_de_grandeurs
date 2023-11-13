from django.shortcuts import render
from .models import Grandeur


# Create your views here.

def detail(request, id):
    grandeur = Grandeur.objects.get(pk=id)
    return render(request, "grandeurs/detail.html", {"grandeur": grandeur})