# Importation des bibliothèques nécessaires
from PIL import Image
import streamlit as st
import random
import os

# Fonction pour redimensionner une image
def redimensionner_image(chemin_image, largeur):
    image = Image.open(chemin_image)
    ratio = largeur / float(image.size[0])
    hauteur = int(float(image.size[1]) * float(ratio))
    image_resized = image.resize((largeur, hauteur), Image.LANCZOS)
    return image_resized

# Fonction pour déterminer le résultat du ShiFuMi
def determine_result(choix_utilisateur, choix_ordinateur):
    if choix_utilisateur == choix_ordinateur:
        return "Égalité"
    elif (
        (choix_utilisateur == "Pierre" and choix_ordinateur == "Ciseaux")
        or (choix_utilisateur == "Feuille" and choix_ordinateur == "Pierre")
        or (choix_utilisateur == "Ciseaux" and choix_ordinateur == "Feuille")
    ):
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné."

# Définir les options possibles
options = ["Pierre", "Feuille", "Ciseaux"]

# Dossier contenant les images
dossier_images = "images"

# Interface utilisateur avec Streamlit
st.title("Jeu ShiFuMi")

# Sélection du choix par l'utilisateur
choix_utilisateur = st.radio("Votre choix :", options)

# Sélection aléatoire du choix de l'ordinateur
choix_ordinateur = random.choice(options)

# Redimensionner et afficher les choix avec les images (taille réduite à 150 pixels)
st.write(f"Vous avez choisi : {choix_utilisateur}")
image_utilisateur = os.path.abspath(os.path.join(dossier_images, f"{choix_utilisateur.lower()}.png"))
image_redimensionnee_utilisateur = redimensionner_image(image_utilisateur, 150)
st.image(image_redimensionnee_utilisateur, caption=choix_utilisateur, use_column_width=False)

st.write(f"L'ordinateur a choisi : {choix_ordinateur}")
image_ordinateur = os.path.join(dossier_images, f"{choix_ordinateur.lower()}.png")
image_redimensionnee_ordinateur = redimensionner_image(image_ordinateur, 150)
st.image(image_redimensionnee_ordinateur, caption=choix_ordinateur, use_column_width=False)

# Déterminer et afficher le résultat
resultat = determine_result(choix_utilisateur, choix_ordinateur)
st.write(f"Résultat : {resultat}")
