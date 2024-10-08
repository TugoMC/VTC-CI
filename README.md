# VTC-CI

## Description

Ce projet Django est conçu pour gérer les opérations d'une entreprise de VTC. Il offre des fonctionnalités pour suivre les dépenses, les revenus, les chauffeurs et les véhicules, facilitant ainsi la gestion quotidienne et l'évolution de l'entreprise.

## Fonctionnalités

* Enregistrement et gestion détaillés des chauffeurs (informations personnelles, licences, etc.)
* Enregistrement et suivi des véhicules (modèle, année, entretien, etc.)
* Historique complet des affectations de chauffeurs aux véhicules

## Technologies Utilisées

* **Django**: Framework web Python robuste pour le développement rapide.
* **Jazzmin**: Application Django pour créer des interfaces d'administration personnalisées et esthétiques.
* **SQLite**: Base de données légère pour le développement local.


### Prérequis
* Python 3.8 ou supérieur
* Git
* Un éditeur de code (Visual Studio Code, PyCharm, etc.)

### Étapes

## Installation

# Cloner le dépôt
git clone https://github.com/TugoMC/VTC-CI

# Accéder au répertoire du projet
cd dash_vtc

# Créer un environnement virtuel et l'activer
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations de la base de données
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Démarrer le serveur de développement (adapter le port si nécessaire)
python manage.py runserver  # Écoute sur toutes les interfaces, port 8080
