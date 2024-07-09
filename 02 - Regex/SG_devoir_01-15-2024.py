############
# OBJECTIF #
############
# Récupérer les noms et prénoms
# 
####### STRATEGY
# Utilisation d'un dictionnaire sur nltk ?
# Cas rencontrés :
# MOTS EN MAJUSCULES : Formater en minuscules (hors sigles)
# NOMS PROPRES :
#       Retirer les pays, régions, villes (dictionary-based)
#       Conserver les couleurs

# Utilisation de regex101
# 


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import os
import string
import re


# STRING DE PONCTUATION
ponctuation = string.punctuation
ponctuation = ponctuation.replace("'()","")
print(ponctuation)

# nltk.download('averaged_perceptron_tagger')

####### FONCTIONS
# REGEX Noms propres
def find_proper_names(text):
    proper_names = re.findall(r"(\b[A-Z][a-z]+\s[A-Z']+[a-z]+\s)([A-Z][a-z]*\b)*", text)
    return text


# CHEMIN DU DOSSIER ACTUEL
current_path = os.path.dirname(os.path.realpath(__file__))
# print(current_path)


# NOM ET CHEMIN DU FICHIER
name_file = "movie_synopsis.xlsx"
path_file = os.path.join(current_path,name_file)
# print(path_file)

###### CRÉATION DU DATAFRAME
df = pd.read_excel(path_file, header=1)
df = df.drop("imdb_id", axis=1)
# movies_df = df["title"]
synopsis_df = df["plot_synopsis"]
# print(df.head())



# # Retrait de la ponctuation
# for ligne in synopsis_df:
#     for punct in ponctuation:
#         ligne = ligne.replace(punct, " ")
#     liste_noms_propres = []

#     mots = word_tokenize(ligne)
#     mots = [mot for mot in mots if mot not in set(stopwords.words("english"))]
#     tagged = nltk.pos_tag(mots)
#     for (mot, tag) in tagged:
#         if tag == "NNP":
#             liste_noms_propres.append(mot)
#     print(liste_noms_propres)

# def extraction_noms_propres(texte):
