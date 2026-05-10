from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Donneur, Hopital
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        role = request.POST.get('role')
        password = request.POST.get('password')
        ville = request.POST.get('ville', '').strip()

        if role == 'donneur':
            username = request.POST.get('username', '').strip()
        else:
            username = request.POST.get('nom_hopital', '').strip()

        if not username or not password:
            return render(request, 'accounts/register.html', {'error': 'Veuillez remplir tous les champs obligatoires.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': "Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre."})

        if role == 'donneur':
            user = User.objects.create_user(username=username, password=password, is_active=True)
            Donneur.objects.create(
                user=user,
                groupe_sanguin=request.POST.get('groupe_sanguin', 'O+'),
                sexe=request.POST.get('sexe', 'M'),
                date_naissance=request.POST.get('date_naissance'),
                ville=ville,
            )
            return redirect('accounts:login')

        else:
            # Hospital: create user as active and validated
            email = request.POST.get('email', '').strip()
            user = User.objects.create_user(username=username, password=password, is_active=True, email=email)
            Hopital.objects.create(
                user=user,
                nom=username,
                adresse=request.POST.get('adresse', ''),
                ville=ville,
                telephone=request.POST.get('telephone', ''),
                est_valide=True,  # Auto-approved on registration
            )
            return render(request, 'accounts/register_success.html', {'nom': username})

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if hasattr(user, 'donneur'):
                return redirect('donneur:dashboard')
            if hasattr(user, 'hopital'):
                return redirect('hopital:dashboard')
            # Superuser/admin
            return redirect('admin:index')

        return render(request, 'accounts/login.html', {'error': 'Identifiants invalides. Veuillez réessayer.'})

    return render(request, 'accounts/login.html')
