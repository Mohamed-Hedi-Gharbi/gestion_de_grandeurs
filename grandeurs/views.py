from django.shortcuts   import render, redirect
from .models.grandeur   import Grandeur
from .models.form       import GrandeurForm


def detail(request, id):
    grandeur = Grandeur.objects.get(pk=id)
    return render(request, "grandeurs/detail.html", {"grandeur": grandeur}) 

def grandeur_list(request):  
    return render(request, "grandeurs/grandeur_list.html", {"grandeurs": Grandeur.objects.all() })  

def new(request):
    if request.method == 'POST':
        form = GrandeurForm(request.POST)

        if form.is_valid():
            print("hedi")
            grandeur = form.save()
            return redirect('detail', id = grandeur.id)
        
        else:
            form = GrandeurForm()

        return render(request, 'grandeurs/new.html', {'form' : form})
    
    return render(request, 'grandeurs/new.html')
