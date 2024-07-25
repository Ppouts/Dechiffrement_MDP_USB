# Script de Brute Force pour Fichiers ZIP et PDF

Ce script Python permet de rechercher et de tenter de découvrir les mots de passe de fichiers ZIP et PDF protégés par mot de passe en utilisant une attaque par force brute avec une liste de mots de passe.

## Prérequis

- Python 3.12
- Bibliothèques Python : `pyzipper`, `pikepdf`

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/Ppouts/Dechiffrement_MDP_USB.git
    ```

2. Installez les dépendances :
    ```bash
    pip install pyzipper pikepdf
    ```

3. Assurez-vous que vous avez un fichier de liste de mots de passe dans le même répertoire que le script, ou modifiez le chemin dans le script pour pointer vers votre propre fichier de mots de passe.

## Utilisation

1. Exécutez le script en ligne de commande :
    ```bash
    python script.py
    ```

2. Fournissez le chemin du répertoire à vérifier lorsque le script vous le demande.

## Fonctionnalités

- **Recherche de fichiers protégés** : Le script parcourt récursivement tous les fichiers d'un répertoire donné.
- **Détection de protection par mot de passe** : Il vérifie si les fichiers ZIP sont protégés par mot de passe avant d'essayer de les déchiffrer.
- **Brute force sur fichiers ZIP** : Utilise une liste de mots de passe pour essayer de déchiffrer les fichiers ZIP protégés.
- **Brute force sur fichiers PDF** : Utilise une liste de mots de passe pour essayer de déchiffrer les fichiers PDF protégés.

## Structure du Code

- `chemin_liste_mots_de_passe` : Chemin vers le fichier contenant la liste des mots de passe.
- `est_zip_protege(chemin_zip)` : Fonction qui vérifie si un fichier ZIP est protégé par mot de passe.
- `brute_force_zip(chemin_zip, chemin_liste_mots_de_passe)` : Fonction qui tente de déchiffrer un fichier ZIP protégé par mot de passe.
- `brute_force_pdf(chemin_pdf, chemin_liste_mots_de_passe)` : Fonction qui tente de déchiffrer un fichier PDF protégé par mot de passe.
- `rechercher_fichiers(chemin_racine)` : Fonction qui parcourt récursivement un répertoire et tente de déchiffrer tous les fichiers ZIP et PDF protégés par mot de passe.

## Exemple de Sortie

Lorsqu'un fichier protégé par mot de passe est trouvé et que le mot de passe est découvert, le script affichera :

```plaintext
Fichier trouvé : chemin/vers/fichier.zip | Mot de passe : mot_de_passe_trouvé
Fichier trouvé : chemin/vers/fichier.pdf | Mot de passe : mot_de_passe_trouvé
