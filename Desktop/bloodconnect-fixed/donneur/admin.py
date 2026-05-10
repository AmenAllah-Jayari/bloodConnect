from django.contrib import admin
from .models import ReponseAppel, Don


@admin.register(ReponseAppel)
class ReponseAppelAdmin(admin.ModelAdmin):
    list_display = ('demande', 'donneur', 'statut', 'date_reponse')
    list_filter = ('statut', 'date_reponse')
    search_fields = ('demande__hopital__nom', 'donneur__user__username')
    readonly_fields = ('date_reponse',)


@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display = ('donneur', 'date_don', 'etablissement', 'enregistre_le')
    list_filter = ('date_don',)
    search_fields = ('donneur__user__username', 'etablissement')
