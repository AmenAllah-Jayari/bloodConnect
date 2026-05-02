from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Donneur, Hopital
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        role = request.POST.get('role')
        password = request.POST.get('password')

        # Ikhtiyar el username 3la 7asb el role[cite: 6]
        username = request.POST.get('username') if role == 'donneur' else request.POST.get('nom_hopital')

        if not username or not password:
            return render(request, 'accounts/register.html', {'error': 'Champs obligatoires'})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username existe déjà'})

        # Création de l'utilisateur[cite: 6]
        user = User.objects.create_user(username=username, password=password)

        if role == 'donneur':
            Donneur.objects.create(
                user=user,
                groupe_sanguin=request.POST.get('groupe_sanguin'),
                sexe=request.POST.get('sexe'),
                date_naissance=request.POST.get('date_naissance'),
                ville=request.POST.get('ville')
            )
        else:
            Hopital.objects.create(
                user=user,
                nom=request.POST.get('nom_hopital'),
                adresse=request.POST.get('adresse'),
                ville=request.POST.get('ville')
            )

        return redirect('login')

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)


            if hasattr(user, 'donneur'):
                return redirect('donneur:dashboard')
            
            if hasattr(user, 'hopital'):
                # Redirection vers le namespace de l'app 'hopital'
                return redirect('hopital:dashboard')

            return redirect('admin:index')

        return render(request, 'accounts/login.html', {'error': 'Identifiants invalides'})
    return render(request, 'accounts/login.html')

