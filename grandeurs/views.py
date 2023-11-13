from django.shortcuts import render
from .models import Grandeur


def detail(request, id):
    grandeur = Grandeur.objects.get(pk=id)
    return render(request, "grandeurs/detail.html", {"grandeur": grandeur}) 

def grandeur_list(request):  # Correction du nom de la fonction
    return render(request, "grandeurs/grandeur_list.html", {"grandeurs": Grandeur.objects.all() })  