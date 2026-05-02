from django.urls import path
from . import views

app_name = 'hopital' # Becha nasta3mlou 'hopital:dashboard'

urlpatterns = [
    path('dashboard/', views.hopital_dashboard, name='dashboard'),
    path('demande/nouvelle/', views.creer_demande, name='creer_demande'),
    path('liste/', views.liste_hopitaux, name='liste_hopitaux'),
]