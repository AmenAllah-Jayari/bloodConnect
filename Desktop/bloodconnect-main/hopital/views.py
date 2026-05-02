from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Hopital # Importi el model mel accounts[cite: 7]
from django.db.models import Q

@login_required
def hopital_dashboard(request):
    # Hné tnajem tzid el logic mta3 el a7sayet w les demandes
    return render(request, 'hopital/hopital_dashboard.html')

@login_required
def creer_demande(request):
    if request.method == "POST":
        # Hné bech njib el data mel formulaire
        groupe = request.POST.get('groupe_sanguin')
        desc = request.POST.get('description')
        
        # B3id chwaya bech n'zidou el logic bech n'sajlouha fil base[cite: 7]
        # tawa bech n'redirektiwek lil dashboard
        return redirect('hopital:dashboard')

    return render(request, 'hopital/creer_demande.html')

def liste_hopitaux(request):
    query = request.GET.get('q') # Nakhou el klem elli fil barre de recherche
    if query:
        # Nlawjou 3la el hôpital bél esm (case-insensitive)
        hopitaux = Hopital.objects.filter(Q(nom__icontains=query))
    else:
        hopitaux = Hopital.objects.all()
    
    return render(request, 'hopital/liste.html', {'hopitaux': hopitaux})