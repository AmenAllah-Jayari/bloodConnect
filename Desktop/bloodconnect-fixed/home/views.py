from django.shortcuts import render
from hopital.models import DemandeUrgente


def home(request):
    # Afficher uniquement les demandes urgentes des hôpitaux validés
    demandes = DemandeUrgente.objects.filter(
        statut='active',
        hopital__est_valide=True
    ).select_related('hopital').order_by('-date_publication')

    return render(
        request,
        'home.html',
        {'demandes': demandes}
    )