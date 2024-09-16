# chauffeur/urls.py
from django.urls import path
from .views import chauffeur_details_view, fire_chauffeur, historique_licenciement
from chauffeur import views



urlpatterns = [
    path('chauffeur/details/<int:id>/', chauffeur_details_view, name='chauffeur_details'),
    path('chauffeur/fire/<int:chauffeur_id>/', fire_chauffeur, name='fire_chauffeur'),
    path('historique/licenciement/', historique_licenciement, name='historique_licenciement'),
]
