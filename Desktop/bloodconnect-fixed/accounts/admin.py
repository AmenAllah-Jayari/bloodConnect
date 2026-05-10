from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html
from .models import Hopital, Donneur


@admin.register(Hopital)
class HopitalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'telephone', 'user', 'date_inscription')
    list_filter = ('ville',)
    search_fields = ('nom', 'adresse', 'ville')
    readonly_fields = ('user', 'date_inscription')

    fieldsets = (
        ('Informations de base', {
            'fields': ('user', 'nom', 'adresse', 'ville', 'telephone')
        }),
        ('Statut', {
            'fields': ('est_valide',)
        }),
        ('Dates', {
            'fields': ('date_inscription',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Donneur)
class DonneurAdmin(admin.ModelAdmin):
    list_display = ('user', 'groupe_sanguin', 'sexe', 'ville', 'telephone', 'actif')
    list_filter = ('groupe_sanguin', 'sexe', 'ville', 'actif')
    search_fields = ('user__username', 'ville', 'telephone')
    readonly_fields = ('user',)
