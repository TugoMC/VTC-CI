# chauffeur/views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone
from chauffeur.models import Chauffeur, HistoriqueLicenciement

def chauffeur_details_view(request, id):
    chauffeur = get_object_or_404(Chauffeur, id=id)
    return render(request, 'admin/chauffeur_details.html', {'chauffeur': chauffeur})

def fire_chauffeur(request, chauffeur_id):
    chauffeur = get_object_or_404(Chauffeur, id=chauffeur_id)

    # Update chauffeur status to terminated
    try:
        chauffeur.status = Chauffeur.STATUS_TERMINATED
        chauffeur.save()

        # Enregistrement du licenciement
        HistoriqueLicenciement.objects.create(
            chauffeur=chauffeur,
            date_licenciement=timezone.now()
        )
        messages.success(request, f"Licenciement de {chauffeur.nom} enregistré avec succès.")
    except Exception as e:
        messages.error(request, f"Erreur lors de l'enregistrement du licenciement: {e}")
        return redirect('chauffeur_details', id=chauffeur.id)
    
    # Rediriger vers la page Jazzmin de l'application chauffeur
    return redirect('/admin/chauffeur/chauffeur/')

def historique_licenciement(request):
    historique = HistoriqueLicenciement.objects.all().order_by('-date_licenciement')
    return render(request, 'admin/historique_licenciement.html', {'historique': historique})
