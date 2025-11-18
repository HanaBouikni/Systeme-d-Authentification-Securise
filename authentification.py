import hashlib
import os
import time
import random
import string
import re

class AuthenticationSystem:
    def __init__(self):
        self.password_file = "password.txt"
        self.failed_attempts = {}
        self.lock_times = {}
    
    def clear_screen(self):
        """Nettoie l'écran de la console"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def validate_username(self, username):
        """
        Valide le nom d'utilisateur selon les critères:
        - Exactement 5 caractères
        - Lettres minuscules uniquement
        """
        if len(username) != 5:
            return False, "Le nom d'utilisateur doit contenir exactement 5 caractères"
        
        if not username.isalpha() or not username.islower():
            return False, "Le nom d'utilisateur doit contenir uniquement des lettres minuscules"
        
        return True, "Nom d'utilisateur valide"
    
    def validate_password(self, password):
        """
        Valide le mot de passe selon les critères:
        - Minimum 8 caractères
        - Contient au moins une minuscule, une majuscule et un chiffre
        """
        if len(password) < 8:
            return False, "Le mot de passe doit contenir au moins 8 caractères"
        
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if not (has_lower and has_upper and has_digit):
            return False, "Le mot de passe doit contenir au moins une minuscule, une majuscule et un chiffre"
        
        return True, "Mot de passe valide"
    
    def generate_salt(self):
        """Génère un salt aléatoire de 5 chiffres"""
        return ''.join(random.choices(string.digits, k=5))
    
    def hash_password(self, password, salt):
        """
        Hash le mot de passe avec le salt en utilisant SHA-256
        Format: hash = SHA256(password + salt)
        """
        salted_password = password + salt
        return hashlib.sha256(salted_password.encode()).hexdigest()
    
    def user_exists(self, username):
        """Vérifie si l'utilisateur existe déjà dans le fichier"""
        try:
            with open(self.password_file, 'r') as file:
                for line in file:
                    if line.startswith(username + ":"):
                        return True
            return False
        except FileNotFoundError:
            return False
    
    def signup(self):
        """Fonction d'inscription d'un nouvel utilisateur"""
        print("\n" + "="*50)
        print("INSCRIPTION")
        print("="*50)
        
        while True:
            username = input("Nom d'utilisateur (5 lettres minuscules): ").strip()
            is_valid, message = self.validate_username(username)
            
            if not is_valid:
                print(f"❌ Erreur: {message}")
                continue
            
            if self.user_exists(username):
                print("❌ Erreur: Ce nom d'utilisateur existe déjà")
                continue
            
            break
        
        while True:
            password = input("Mot de passe (min 8 caractères, avec majuscule, minuscule, chiffre): ").strip()
            is_valid, message = self.validate_password(password)
            
            if not is_valid:
                print(f"❌ Erreur: {message}")
                continue
            
            break
        
        # Génération du salt et hashage
        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        
        # Sauvegarde dans le fichier
        with open(self.password_file, 'a') as file:
            file.write(f"{username}:{salt}:{hashed_password}\n")
        
        print("✅ Compte créé avec succès!")
        print(f"📝 Salt généré: {salt}")
        print(f"🔒 Hash stocké: {hashed_password}")
        input("Appuyez sur Entrée pour continuer...")
    
    def is_account_locked(self, username):
        """Vérifie si le compte est temporairement bloqué"""
        if username in self.lock_times:
            remaining_time = self.lock_times[username] - time.time()
            if remaining_time > 0:
                print(f"🔒 Compte temporairement bloqué. Temps restant: {int(remaining_time)} secondes")
                return True
            else:
                # Débloquer le compte si le temps est écoulé
                del self.lock_times[username]
        return False
    
    def get_lock_duration(self, failed_count):
        """Retourne la durée de blocage selon le nombre d'échecs"""
        if failed_count <= 3:
            return 5
        elif failed_count <= 6:
            return 10
        elif failed_count <= 9:
            return 15
        else:
            return 20
    
    def signin(self):
        """Fonction de connexion avec gestion des tentatives échouées"""
        print("\n" + "="*50)
        print("CONNEXION")
        print("="*50)
        
        username = input("Nom d'utilisateur: ").strip()
        
        # Vérification du format du nom d'utilisateur
        is_valid, message = self.validate_username(username)
        if not is_valid:
            print(f"❌ {message}")
            input("Appuyez sur Entrée pour continuer...")
            return
        
        # Vérification si le compte est bloqué
        if self.is_account_locked(username):
            input("Appuyez sur Entrée pour continuer...")
            return
        
        # Vérification si l'utilisateur existe
        user_data = None
        try:
            with open(self.password_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(':')
                    if len(parts) == 3 and parts[0] == username:
                        user_data = {
                            'username': parts[0],
                            'salt': parts[1],
                            'hash': parts[2]
                        }
                        break
        except FileNotFoundError:
            print("❌ Aucun utilisateur enregistré")
            input("Appuyez sur Entrée pour continuer...")
            return
        
        if not user_data:
            print("❌ Utilisateur non trouvé")
            input("Appuyez sur Entrée pour continuer...")
            return
        
        # Gestion des tentatives de mot de passe
        password = input("Mot de passe: ").strip()
        
        # Calcul du hash pour vérification
        calculated_hash = self.hash_password(password, user_data['salt'])
        
        if calculated_hash == user_data['hash']:
            # Connexion réussie
            print("✅ Connexion réussie!")
            self.failed_attempts[username] = 0  # Réinitialiser les tentatives échouées
            input("Appuyez sur Entrée pour continuer...")
        else:
            # Mot de passe incorrect
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            failed_count = self.failed_attempts[username]
            
            print(f"❌ Mot de passe incorrect. Tentative {failed_count}/3")
            
            if failed_count >= 3:
                lock_duration = self.get_lock_duration(failed_count)
                
                if failed_count >= 12:  # Après 12 tentatives échouées
                    print("🚫 Compte banni définitivement!")
                    # Ici on pourrait implémenter un bannissement permanent
                    input("Appuyez sur Entrée pour continuer...")
                    return
                
                print(f"🔒 Compte bloqué pendant {lock_duration} secondes")
                self.lock_times[username] = time.time() + lock_duration
                
                # Attente du déblocage
                for i in range(lock_duration, 0, -1):
                    print(f"Temps restant: {i} secondes", end='\r')
                    time.sleep(1)
                print("Compte débloqué! Vous pouvez réessayer.")
            
            input("Appuyez sur Entrée pour continuer...")
    
    def display_menu(self):
        """Affiche le menu principal"""
        self.clear_screen()
        print("🔐 SYSTÈME D'AUTHENTIFICATION SÉCURISÉ")
        print("="*40)
        print("1. S'inscrire (Sign Up)")
        print("2. Se connecter (Sign In)")
        print("3. Quitter (Exit)")
        print("="*40)
    
    def run(self):
        """Boucle principale du programme"""
        while True:
            self.display_menu()
            choice = input("Choisissez une option (1-3): ").strip()
            
            if choice == '1':
                self.signup()
            elif choice == '2':
                self.signin()
            elif choice == '3':
                print("👋 Au revoir!")
                break
            else:
                print("❌ Option invalide. Veuillez choisir 1, 2 ou 3.")
                input("Appuyez sur Entrée pour continuer...")

# Fonction de démonstration du système
def demonstrate_system():
    """Fonction pour démontrer le fonctionnement du système"""
    print("🔍 DÉMONSTRATION DU SYSTÈME D'AUTHENTIFICATION")
    print("="*50)
    
    auth_system = AuthenticationSystem()
    
    # Création d'un exemple de fichier password
    print("\n1. Structure du fichier password.txt:")
    print("   Format: username:salt:hash")
    print("   Exemple: alice:12345:a1b2c3d4e5f6...")
    
    print("\n2. Processus d'inscription:")
    print("   - Validation du nom d'utilisateur (5 lettres minuscules)")
    print("   - Validation du mot de passe (8+ caractères avec complexité)")
    print("   - Génération d'un salt aléatoire")
    print("   - Hashage: SHA256(password + salt)")
    print("   - Stockage dans le fichier")
    
    print("\n3. Processus de connexion:")
    print("   - Vérification du format du nom d'utilisateur")
    print("   - Vérification du blocage temporaire")
    print("   - Lecture du salt et hash stockés")
    print("   - Calcul du hash avec le mot de passe saisi")
    print("   - Comparaison des hashs")
    
    print("\n4. Gestion des échecs:")
    print("   - 1-2 échecs: Message d'erreur")
    print("   - 3 échecs: Blocage 5 secondes")
    print("   - 6 échecs: Blocage 10 secondes")
    print("   - 9 échecs: Blocage 15 secondes")
    print("   - 12 échecs: Compte banni")
    
    input("\nAppuyez sur Entrée pour lancer le système...")

# Point d'entrée principal
if __name__ == "__main__":
    demonstrate_system()
    
    # Lancement du système d'authentification
    auth_system = AuthenticationSystem()
    auth_system.run()