from django.contrib import admin
from .models import DemandeUrgente

@admin.register(DemandeUrgente)
class DemandeUrgenteAdmin(admin.ModelAdmin):
    list_display = ('hopital', 'groupe_sanguin', 'quantite', 'statut', 'date_publication')
    list_filter = ('statut', 'groupe_sanguin', 'date_publication')
    search_fields = ('hopital__nom', 'description')
    readonly_fields = ('date_publication', 'hopital')
    fieldsets = (
        ('Informations de la demande', {
            'fields': ('hopital', 'groupe_sanguin', 'quantite')
        }),
        ('Détails', {
            'fields': ('description', 'delai', 'statut')
        }),
        ('Dates', {
            'fields': ('date_publication',)
        }),
    )
