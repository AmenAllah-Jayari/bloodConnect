from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Donneur, Hopital
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 1. AHAM KHOTWA: Nasn3ou el User w nkhabiweh fi variable ismha 'user'
        user = User.objects.create_user(username=username, password=password)

        # 2. Tawa nasta3mlou 'user' elli sna3neha lfoq
        if role == 'donneur':
            Donneur.objects.create(
                user=user,  # Tawa 'user' wallet m3arfa
                groupe_sanguin=request.POST.get('groupe_sanguin'),
                sexe=request.POST.get('sexe'),
                date_naissance=request.POST.get('date_naissance'),
                ville=request.POST.get('ville')
            )
        elif role == 'hopital':
            Hopital.objects.create(
                user=user,
                nom=request.POST.get('nom_hopital'),
                adresse=request.POST.get('adresse'),
                agrement=request.POST.get('agrement'),
                ville=request.POST.get('ville')
            )
        return redirect('login')
    
    return render(request, 'accounts/register.html')




def user_login(request):
    if request.method == "POST":
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        user = authenticate(request, username=u_name, password=p_word)

        if user is not None:
            login(request, user)
            
            # Vérification du rôle pour la redirection
            if hasattr(user, 'donneur'):
                return redirect('donneur_dashboard')
            elif hasattr(user, 'hopital'):
                return redirect('hopital_dashboard')
            else:
                return redirect('admin:index') # Redirection vers l'admin si c'est un superuser
        else:
            # Tu peux ajouter un message d'erreur ici
            return render(request, 'accounts/login.html', {'error': 'Identifiants invalides'})

    return render(request, 'accounts/login.html')

@login_required
def donneur_dashboard(request):
    return render(request, 'accounts/donneur_dashboard.html')