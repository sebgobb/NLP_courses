import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import os
import string

ponctuation = string.punctuation

# nltk.download('averaged_perceptron_tagger')
current_path = os.getcwd()
name_file = "movie_synopsis.xlsx"
path_file = os.path.join(current_path,name_file)

df = pd.read_excel(path_file, header=1)
movies_df = df["title"]
synopsis_df = df["plot_synopsis"]
for ligne in synopsis_df:
    for punct in ponctuation:
        ligne = ligne.replace(punct, " ")
    liste_noms_propres = []

    mots = word_tokenize(ligne)
    mots = [mot for mot in mots if mot not in set(stopwords.words("english"))]
    tagged = nltk.pos_tag(mots)
    for (mot, tag) in tagged:
        if tag == "NNP":
            liste_noms_propres.append(mot)
    print(liste_noms_propres)

# def extraction_noms_propres(texte):
