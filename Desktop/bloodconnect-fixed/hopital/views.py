from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Hopital
from hopital.models import DemandeUrgente
from hopital.forms import DemandeUrgenteForm
from donneur.models import ReponseAppel, Don
from django.db.models import Q


@login_required
def hopital_dashboard(request):
    try:
        hopital = Hopital.objects.get(user=request.user)
    except Hopital.DoesNotExist:
        return redirect('accounts:login')

    if not hopital.est_valide:
        return render(request, 'hopital/hopital_en_attente.html', {'hopital': hopital})

    demandes = hopital.demandes.all().order_by('-date_publication')
    demandes_actives = demandes.filter(statut='active').count()
    total_demandes = demandes.count()

    # Réponses en attente de confirmation pour cet hôpital
    reponses_en_attente = ReponseAppel.objects.filter(
        demande__hopital=hopital,
        statut='En attente'
    ).select_related('donneur__user', 'demande').order_by('-date_reponse')

    return render(request, 'hopital/hopital_dashboard.html', {
        'demandes': demandes,
        'demandes_actives': demandes_actives,
        'total_demandes': total_demandes,
        'hopital': hopital,
        'reponses_en_attente': reponses_en_attente,
    })


@login_required
def confirmer_reponse(request, reponse_id):
    """Confirme une réponse → crée automatiquement un Don."""
    try:
        hopital = Hopital.objects.get(user=request.user)
    except Hopital.DoesNotExist:
        return redirect('accounts:login')

    reponse = get_object_or_404(ReponseAppel, id=reponse_id, demande__hopital=hopital)

    # Créer le don automatiquement
    don, created = Don.objects.get_or_create(
        donneur=reponse.donneur,
        date_don=timezone.now().date(),
        etablissement=hopital.nom,
        defaults={'notes': f"Don suite à l'appel urgent #{reponse.demande.id}"}
    )

    reponse.statut = 'Confirmé'
    reponse.save()

    messages.success(
        request,
        f"✓ Don de {reponse.donneur.user.username} confirmé et enregistré automatiquement."
    )
    return redirect('hopital:dashboard')


@login_required
def refuser_reponse(request, reponse_id):
    """Refuse une réponse de donneur."""
    try:
        hopital = Hopital.objects.get(user=request.user)
    except Hopital.DoesNotExist:
        return redirect('accounts:login')

    reponse = get_object_or_404(ReponseAppel, id=reponse_id, demande__hopital=hopital)
    reponse.statut = 'Refusé'
    reponse.save()

    messages.info(request, f"Réponse de {reponse.donneur.user.username} refusée.")
    return redirect('hopital:dashboard')


@login_required
def creer_demande(request):
    try:
        hopital = Hopital.objects.get(user=request.user)
    except Hopital.DoesNotExist:
        return redirect('accounts:login')

    if not hopital.est_valide:
        return redirect('hopital:dashboard')

    if request.method == "POST":
        form = DemandeUrgenteForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.hopital = hopital
            demande.statut = 'active'
            demande.save()
            return redirect('hopital:dashboard')
    else:
        form = DemandeUrgenteForm()

    return render(request, 'hopital/creer_demande.html', {'form': form})


def liste_hopitaux(request):
    query = request.GET.get('q')
    if query:
        hopitaux = Hopital.objects.filter(
            Q(nom__icontains=query) | Q(ville__icontains=query),
            est_valide=True
        )
    else:
        hopitaux = Hopital.objects.filter(est_valide=True)

    return render(request, 'hopital/liste.html', {'hopitaux': hopitaux, 'query': query or ''})