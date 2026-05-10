from django.urls import path
from . import views

app_name = 'hopital'

urlpatterns = [
    path('dashboard/', views.hopital_dashboard, name='dashboard'),
    path('demande/nouvelle/', views.creer_demande, name='creer_demande'),
    path('liste/', views.liste_hopitaux, name='liste_hopitaux'),
    path('reponse/<int:reponse_id>/confirmer/', views.confirmer_reponse, name='confirmer_reponse'),
    path('reponse/<int:reponse_id>/refuser/', views.refuser_reponse, name='refuser_reponse'),
]