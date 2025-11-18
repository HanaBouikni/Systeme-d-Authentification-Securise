
# 🔐 Système d'Authentification Sécurisé

## 📋 Table des Matières

-   [Description du Projet](#-description-du-projet)
-   [Fonctionnalités](#-fonctionnalités)
-   [Architecture du Système](#-architecture-du-système)
-   [Installation et Exécution](#-installation-et-exécution)
-   [Structure du Code](#-structure-du-code)
-   [Sécurité Implémentée](#-sécurité-implémentée)
-   [Exemples d'Utilisation](#-exemples-dutilisation)


------------------------------------------------------------------------

## 🔐 Description du Projet

Ce projet implémente un **système d'authentification sécurisé en
Python** avec gestion des utilisateurs, validation stricte des
identifiants et protection contre les attaques par force brute.

### 🎯 Objectifs pédagogiques

-   Comprendre les mécanismes d'authentification\
-   Implémenter le hachage sécurisé des mots de passe\
-   Gérer les politiques de sécurité des mots de passe\
-   Protéger contre les attaques par brute force

------------------------------------------------------------------------

## 🚀 Fonctionnalités

### ✅ Inscription (Sign Up)

-   Validation du nom d'utilisateur (5 lettres minuscules exactement)
-   Validation du mot de passe (8+ caractères avec majuscule, minuscule,
    chiffre)
-   Génération automatique d'un **salt** aléatoire
-   Hachage sécurisé **SHA256**
-   Stockage des informations dans un fichier texte

### 🔑 Connexion (Sign In)

-   Vérification des identifiants
-   Comptabilisation des tentatives échouées
-   Blocage du compte après plusieurs échecs
-   Bannissement définitif après 12 échecs

### ⏰ Système de Blocage Progressif

  Tentatives Échouées   Durée de Blocage
  --------------------- ------------------
  3                     5 secondes
  6                     10 secondes
  9                     15 secondes
  12                    Bannissement

------------------------------------------------------------------------

## 🏗️ Architecture du Système

``` mermaid
graph TD
    A[Programme Principal] --> B[Menu Principal]
    B --> C[Inscription]
    B --> D[Connexion]
    B --> E[Quitter]

    C --> C1[Validation Username]
    C --> C2[Validation Password]
    C --> C3[Génération Salt]
    C --> C4[Hachage SHA256]
    C --> C5[Sauvegarde Fichier]

    D --> D1[Vérification Blocage]
    D --> D2[Lecture Fichier]
    D --> D3[Calcul Hash]
    D --> D4[Comparaison]
    D --> D5[Gestion Échecs]

    D5 --> D6[Compte Bloqué]
    D5 --> D7[Compte Banni]

    F[Fichier password.txt] --> C5
    F --> D2
```

------------------------------------------------------------------------

## 📥 Installation et Exécution

### 🔧 Prérequis

-   Python **3.6+**
-   Aucun package externe nécessaire

### ▶️ Lancer le Programme

``` bash
# Cloner le repository
git clone https://github.com/votre-username/authentication-system.git
cd authentication-system

# Exécuter
python authentication_system.py
```

------------------------------------------------------------------------

## 🗂️ Structure du Code

    authentication-system/
    │
    ├── authentication_system.py  # Code principal
    ├── password.txt              # Stockage des utilisateurs (généré automatiquement)
    ├── README.md                 # Documentation
    └── requirements.txt          # Vide (bibliothèques standard utilisées)

------------------------------------------------------------------------

## ⚙️ Classes Principales

### `AuthenticationSystem`

Gère l'ensemble du processus d'authentification.

#### Méthodes principales

-   `validate_username()`
-   `validate_password()`
-   `generate_salt()`
-   `hash_password()`
-   `signup()`
-   `signin()`
-   `is_account_locked()`

------------------------------------------------------------------------

## 🔒 Sécurité Implémentée

### 1. Hachage Sécurisé

``` python
def hash_password(self, password, salt):
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode()).hexdigest()
```

### 2. Salt Aléatoire

-   5 chiffres générés aléatoirement\
-   Unique pour chaque utilisateur\
-   Protège contre les rainbow tables

### 3. Validation Stricte

#### Username :

-   5 lettres\
-   minuscules uniquement

#### Mot de passe :

-   minimum 8 caractères\
-   au moins une majuscule\
-   au moins une minuscule\
-   au moins un chiffre

### 4. Protection Force Brute

-   Compteur de tentatives échouées\
-   Blocage progressif\
-   Bannissement définitif après 12 échecs

------------------------------------------------------------------------

## 💻 Exemples d'Utilisation

### 📌 Scénario 1 : Inscription Réussie

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
    Nom d'utilisateur : alice
    Mot de passe : Pass1234
    ✅ Compte créé avec succès!
    📝 Salt généré : 12345
    🔒 Hash stocké : a1b2c3d4e5f6...

### 📌 Scénario 2 : Connexion avec Échecs

    ==================================================
    CONNEXION
    ==================================================
    Nom d'utilisateur : alice
    Mot de passe : wrongpass
    ❌ Mot de passe incorrect. Tentative 1/3

    Mot de passe : wrongpass
    ❌ Tentative 2/3

    Mot de passe : wrongpass
    ❌ Tentative 3/3
    🔒 Compte bloqué pendant 5 secondes

------------------------------------------------------------------------

## 📄 Format du Fichier `password.txt`

    username:salt:hash
    alice:12345:a1b2c3d4e5f6...
    bob:67890:b2c3d4e5f6g7...

------------------------------------------------------------------------

## 🛠️ Développement

Le fichier `authentication_system.py` contient :

-   Menu interactif\
-   Validation des entrées\
-   Génération de salt\
-   Hachage sécurisé\
-   Gestion des blocages\
-   Lecture/écriture dans `password.txt`

### Démonstration interne

``` python
demonstrate_system()
```


