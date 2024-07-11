# Regex exercises
## Strategy
The aim is to retrieve the full name of each character/actor contained in the "synopsis" column of the "movie_synopsis.xlsx" dataframe.

The strategy adopted is to use Regex to focus on groups of words beginning with a capital letter. The Regex formula allows us to focus on groups containing 2 and 3 entities (example: George W. Bush).

In addition, the use of wordnet, stopwords and webcolors dictionaries are subtracted from the word groups to ensure relevant results.

## Export
A new dataframe is created containing :
- a column for potential full names
- a column for real full names

Dataframe is saved as "OUTPUT_proper_names.xlsx"
