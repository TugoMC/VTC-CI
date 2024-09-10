# entrees/admin.py

from django.contrib import admin
from .models import RevenuJournalier

@admin.register(RevenuJournalier)
class RevenuJournalierAdmin(admin.ModelAdmin):
    list_display = ('chauffeur', 'vehicule', 'date', 'montant')
    list_filter = ('chauffeur', 'vehicule', 'date')
    search_fields = ('chauffeur__nom', 'vehicule__immatriculation', 'date')
    ordering = ('-date',)
