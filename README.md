# 🔐 Système d'Authentification Sécurisé

## 📋 Table des Matières
- [Description du Projet](#description-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Architecture du Système](#architecture-du-système)
- [Installation et Exécution](#installation-et-exécution)
- [Structure du Code](#structure-du-code)
- [Sécurité Implémentée](#sécurité-implémentée)
- [Exemples d'Utilisation](#exemples-dutilisation)
- [Auteur](#auteur)

## 🔐 Description du Projet

Ce projet implémente un système d'authentification sécurisé en Python avec gestion des utilisateurs, validation stricte des identifiants et protection contre les attaques par force brute.

**Objectifs pédagogiques:**
- Comprendre les mécanismes d'authentification
- Implémenter le hachage sécurisé des mots de passe
- Gérer les politiques de sécurité des mots de passe
- Protéger contre les attaques par brute force

## 🚀 Fonctionnalités

### ✅ Inscription (Sign Up)
- Validation du nom d'utilisateur (5 lettres minuscules exactement)
- Validation du mot de passe (8+ caractères avec majuscule, minuscule, chiffre)
- Génération automatique d'un salt aléatoire
- Hachage SHA256 du mot de passe
- Stockage sécurisé dans un fichier texte

### 🔑 Connexion (Sign In)
- Vérification des identifiants
- Gestion progressive des tentatives échouées
- Blocage temporaire après 3 échecs
- Bannissement après 12 échecs

### ⏰ Système de Blocage Progressif
| Tentatives Échouées | Durée de Blocage |
|---------------------|------------------|
| 3                   | 5 secondes       |
| 6                   | 10 secondes      |
| 9                   | 15 secondes      |
| 12                  | Bannissement     |

## 🏗️ Architecture du Système

```mermaid
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
