from django.urls import path
from . import views

app_name = 'donneur'

urlpatterns = [
    path('dashboard/', views.donneur_dashboard, name='dashboard'),
    path('repondre/<int:demande_id>/', views.repondre_appel, name='repondre_appel'),
    path('toggle-actif/', views.toggle_actif, name='toggle_actif'),
]