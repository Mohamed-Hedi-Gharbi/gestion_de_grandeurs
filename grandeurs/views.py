from django.shortcuts import render
from .models import Grandeur


# Create your views here.

def detail(request, id):
    grandeur = Grandeur.objects.get(pk=id)
    return render(request, "grandeurs/detail.html", {"grandeur": grandeur})


def grnadeur_list(request):
    return render(request, "grandeurs/grandeur_list.html", {"grandeurs", Grandeur.objects.all() })

