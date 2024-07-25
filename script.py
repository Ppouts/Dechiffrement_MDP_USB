import os
import pyzipper
import pikepdf

chemin_liste_mots_de_passe = r"Nom\de\la\liste\de\mots\de\passe.txt"

def est_zip_protege(chemin_zip):
    try:
        with pyzipper.AESZipFile(chemin_zip) as zf:
            for info in zf.infolist():
                if info.flag_bits & 0x1:  
                    return True
        return False
    except pyzipper.BadZipFile:
        print(f"Fichier ZIP invalide: {chemin_zip}") 
        return False
    except Exception as e:
        print(f"Erreur lors de la vérification du ZIP: {e}")
        return False

def brute_force_zip(chemin_zip, chemin_liste_mots_de_passe):
    if not est_zip_protege(chemin_zip):
        # Ne pas afficher les fichiers ZIP non protégés
        # print(f"Fichier ZIP non protégé : {chemin_zip}")
        return None
    try:
        with open(chemin_liste_mots_de_passe, 'r', encoding='utf-8') as wordlist:
            for mot_de_passe in wordlist:
                mot_de_passe = mot_de_passe.strip()
                try:
                    with pyzipper.AESZipFile(chemin_zip) as zf:
                        zf.extractall(pwd=mot_de_passe.encode())
                        return mot_de_passe
                except pyzipper.BadZipFile:
                    print(f"Fichier ZIP invalide: {chemin_zip}") 
                    return None
                except Exception as e:
                    continue
        print(f"Mot de passe non trouvé dans la liste pour le fichier : {chemin_zip}")
        return None
    except Exception as e:
        print(f"Erreur lors de la brute-force ZIP : {e}")
        return None

def brute_force_pdf(chemin_pdf, chemin_liste_mots_de_passe):
    try:
        with open(chemin_liste_mots_de_passe, 'r', encoding='utf-8') as wordlist:
            for mot_de_passe in wordlist:
                mot_de_passe = mot_de_passe.strip()
                try:
                    with pikepdf.open(chemin_pdf, password=mot_de_passe) as pdf:
                        return mot_de_passe
                except pikepdf.PasswordError:
                    continue
                except pikepdf._qpdf.PasswordError:
                    continue
                except pikepdf.PermissionsError:
                    return mot_de_passe
        print(f"Mot de passe non trouvé dans la liste pour le fichier : {chemin_pdf}")
        return None
    except pikepdf.PasswordError:
        print(f"Mot de passe non trouvé pour le fichier : {chemin_pdf}")
        return None
    except Exception as e:
        print(f"Erreur lors de l'utilisation de pikepdf : {e}")
        return None

def rechercher_fichiers(chemin_racine):
    resultats = []
    for dossier, sous_dossiers, fichiers in os.walk(chemin_racine):
        for fichier in fichiers:
            chemin_fichier = os.path.join(dossier, fichier)
            if fichier.endswith('.zip'):
                mot_de_passe = brute_force_zip(chemin_fichier, chemin_liste_mots_de_passe)
                if mot_de_passe and mot_de_passe != "null":
                    resultats.append((chemin_fichier, mot_de_passe))
            elif fichier.endswith('.pdf'):
                mot_de_passe = brute_force_pdf(chemin_fichier, chemin_liste_mots_de_passe)
                if mot_de_passe and mot_de_passe != "null":
                    resultats.append((chemin_fichier, mot_de_passe))
    return resultats

if __name__ == "__main__":
    chemin_racine = input("Veuillez fournir le chemin a verifier : ")
    if not os.path.exists(chemin_racine):
        print("Le chemin fourni n'existe pas.")
    else:
        resultats = rechercher_fichiers(chemin_racine)
        if resultats:    
            for chemin_fichier, mot_de_passe in resultats:
                print(f"Fichier trouvé : {chemin_fichier} | Mot de passe : {mot_de_passe}")
        else:
            print("Aucun fichier protégé par mot de passe n'a été trouvé.")
            
            
# archive rar zip 7zip 

# partion vera cryp 