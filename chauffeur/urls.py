# chauffeur/urls.py
from django.urls import path
from .views import chauffeur_details_view

urlpatterns = [
    path('details/<int:id>/', chauffeur_details_view, name='chauffeur_details'),
    # autres URLs
]
