from django.db import models
from accounts.models import Hopital


class DemandeUrgente(models.Model):
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name='demandes')
    groupe_sanguin = models.CharField(max_length=5)
    quantite = models.IntegerField(help_text="Nombre de poches")
    delai = models.DateField()
    statut = models.CharField(max_length=20, default='active')
    description = models.TextField(blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.groupe_sanguin} - {self.hopital.nom}"
