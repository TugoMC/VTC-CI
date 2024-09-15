# vehicules/urls.py
from django.urls import path
from .views import vehicule_details_view

urlpatterns = [
    path('details/<int:id>/', vehicule_details_view, name='vehicule_details'),
    # autres URLs
]
