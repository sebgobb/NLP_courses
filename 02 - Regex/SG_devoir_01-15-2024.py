############
# OBJECTIVE #
############
# To retrieve groups of proper names of characters/actors
# 
####### STRATEGY
# Use dictionaries from STOPWORDS, WORDNET (via nltk)
# Use WEBCOLORS color dictionary
# Cases encountered :
# UPPERCASE WORDS: Format in lower case (excluding acronyms)
# PROPER NOUNS :
# Remove countries, regions, cities (dictionary-based)
# Keep colors

# Use of regex101.com

import webcolors
from nltk.corpus import wordnet, stopwords
import pandas as pd
import os
import re

# CURRENT FOLDER PATH
current_path = os.path.dirname(os.path.realpath(__file__))
# print(current_path)

# INPUT FILE NAME AND PATH
name_file = "movie_synopsis.xlsx"
path_file = os.path.join(current_path,name_file)
# print(path_file)


####### DICTIONNARIES
# stopwords
stopwords_list = set(stopwords.words())

# words
wordnet_list = set(wordnet.words())

# colors
css3_color_names = webcolors._definitions._CSS3_NAMES_TO_HEX.keys()
colors_to_del = [
    "red",
    "black",
    "white",
    "silver",
    "brown",
    "gold"
]
colors_list = [c for c in css3_color_names if c not in colors_to_del]
# print(css3_color_names)


####### FUNCTIONS
# REGEX retrieves likely groups of proper names
def find_probable_proper_names_group(text):
    proper_names_list = re.findall(r"\b[A-Z][a-z]+\s[A-Z'.]+[a-z]*\s[A-Z][a-z]*\b|\b[A-Z][a-z]+\s[A-Z']+[a-z]+\b", text)
    return proper_names_list

# Delete bad groups of proper names containing names
def delete_wrong_proper_names_groups(list):
    new_list = []
    for png in list:
        png_lowercased = png.lower()
        png_lc_list = png_lowercased.split()
        valid_png = True
        for word in png_lc_list:
            # Checks whether one of the words in the group of proper names is contained in the "wordnet" dictionary and outside the "webcolors" dictionary
            if word in colors_list:
                break
            elif any(word in dico for dico in [stopwords_list, wordnet_list]):
                valid_png = False
                break
        if valid_png and png not in new_list:
            new_list.append(png)
    return new_list


###### DATAFRAME CREATION
# Reading input file
df = pd.read_excel(path_file, header=1)

# Lauching functions
df["Probable proper names"] = df["plot_synopsis"].apply(find_probable_proper_names_group)
df["Real proper names"] = df["Probable proper names"].apply(delete_wrong_proper_names_groups)

# Deleting imdb_id's movie and plot_synopsis
df = df.drop(["imdb_id", "plot_synopsis"], axis=1)


####### SAVE DATAFRAME
df.to_excel(os.path.join(current_path,"OUTPUT_proper_names.xlsx"), index=False)