from django.shortcuts import render
from grandeurs.models import Grandeur

# Create your views here.


def home_view(request):
    context = {'grandeurs': Grandeur.objects.all()}
    return render(request, "website/home.html", context = context)


