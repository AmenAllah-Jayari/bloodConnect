from django.urls import path
from . import views

app_name = 'donneur' # Becha nasta3mlou 'donneur:dashboard'[cite: 8]

urlpatterns = [
    path('dashboard/', views.donneur_dashboard, name='dashboard'),
]