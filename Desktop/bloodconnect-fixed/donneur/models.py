from django.db import models
from datetime import timedelta
from accounts.models import Donneur


class Don(models.Model):
    donneur = models.ForeignKey(Donneur, on_delete=models.CASCADE, related_name='dons')
    date_don = models.DateField()
    etablissement = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    enregistre_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_don']

    def __str__(self):
        return f"{self.donneur} – {self.date_don} à {self.etablissement}"

    def prochaine_date_eligibilite(self):
        """56 jours pour hommes, 84 jours pour femmes."""
        delai = 84 if self.donneur.sexe == 'F' else 56
        return self.date_don + timedelta(days=delai)


class ReponseAppel(models.Model):
    demande = models.ForeignKey('hopital.DemandeUrgente', on_delete=models.CASCADE, related_name='reponses')
    donneur = models.ForeignKey(Donneur, on_delete=models.CASCADE)
    date_reponse = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='En attente')

    class Meta:
        unique_together = ('demande', 'donneur')

    def __str__(self):
        return f"{self.donneur} → {self.demande}"
