README - Système d'Authentification Sécurisé
📋 Table des Matières
Description du Projet

Fonctionnalités

Architecture du Système

Installation et Exécution

Structure du Code

Sécurité Implémentée

Exemples d'Utilisation

Auteur

🔐 Description du Projet
Ce projet implémente un système d'authentification sécurisé en Python avec gestion des utilisateurs, validation stricte des identifiants et protection contre les attaques par force brute.

Objectifs pédagogiques:

Comprendre les mécanismes d'authentification

Implémenter le hachage sécurisé des mots de passe

Gérer les politiques de sécurité des mots de passe

Protéger contre les attaques par brute force

🚀 Fonctionnalités
✅ Inscription (Sign Up)
Validation du nom d'utilisateur (5 lettres minuscules exactement)

Validation du mot de passe (8+ caractères avec majuscule, minuscule, chiffre)

Génération automatique d'un salt aléatoire

Hachage SHA256 du mot de passe

Stockage sécurisé dans un fichier texte

🔑 Connexion (Sign In)
Vérification des identifiants

Gestion progressive des tentatives échouées

Blocage temporaire après 3 échecs

Bannissement après 12 échecs

⏰ Système de Blocage Progressif
Tentatives Échouées	Durée de Blocage
3	5 secondes
6	10 secondes
9	15 secondes
12	Bannissement
🏗️ Architecture du Système


















📥 Installation et Exécution
Prérequis
Python 3.6 ou supérieur

Aucune installation de packages externes nécessaire

Lancement du Programme
bash
# Cloner le repository
git clone https://github.com/votre-username/authentication-system.git
cd authentication-system

# Exécuter le programme
python authentication_system.py
🗂️ Structure du Code
text
authentication-system/
│
├── authentication_system.py  # Code source principal
├── password.txt             # Fichier de stockage des utilisateurs
└── README.md               # Documentation
Classes Principales
AuthenticationSystem
Classe principale gérant tout le système d'authentification.

Méthodes principales:

validate_username(): Validation format username

validate_password(): Validation politique mot de passe

generate_salt(): Génération salt aléatoire

hash_password(): Hachage SHA256

signup(): Processus d'inscription

signin(): Processus de connexion

is_account_locked(): Vérification blocage compte

🔒 Sécurité Implémentée
1. Hachage Sécurisé
python
def hash_password(self, password, salt):
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode()).hexdigest()
2. Salt Aléatoire
5 chiffres générés aléatoirement

Unique pour chaque utilisateur

Empêche les attaques par rainbow table

3. Validation Stricte
Username:

Exactement 5 caractères

Lettres minuscules uniquement

Password:

Minimum 8 caractères

Au moins une majuscule

Au moins une minuscule

Au moins un chiffre

4. Protection Force Brute
Compteur de tentatives échouées

Blocage temporel progressif

Bannissement définitif après 12 échecs

💻 Exemples d'Utilisation
Scénario 1: Inscription Réussie
text
🔐 SYSTÈME D'AUTHENTIFICATION SÉCURISÉ
========================================
1. S'inscrire (Sign Up)
2. Se connecter (Sign In)
3. Quitter (Exit)
========================================
Choisissez une option (1-3): 1

==================================================
INSCRIPTION
==================================================
Nom d'utilisateur (5 lettres minuscules): alice
Mot de passe (min 8 caractères, avec majuscule, minuscule, chiffre): Pass1234
✅ Compte créé avec succès!
📝 Salt généré: 12345
🔒 Hash stocké: a1b2c3d4e5f6...
Scénario 2: Connexion avec Échecs
text
==================================================
CONNEXION
==================================================
Nom d'utilisateur: alice
Mot de passe: wrongpass
❌ Mot de passe incorrect. Tentative 1/3

Mot de passe: wrongpass
❌ Mot de passe incorrect. Tentative 2/3

Mot de passe: wrongpass  
❌ Mot de passe incorrect. Tentative 3/3
🔒 Compte bloqué pendant 5 secondes
Format du Fichier de Stockage
text
username:salt:hash
alice:12345:a1b2c3d4e5f6...
bob:67890:b2c3d4e5f6g7...
🛠️ Développement
Ajouter de Nouvelles Fonctionnalités
python
# Exemple: Ajouter la gestion des administrateurs
def is_admin(self, username):
    # Implémentation de la vérification admin
    pass
Tests
Le programme inclut une fonction de démonstration automatique:

python
demonstrate_system()  # Affiche le fonctionnement du système