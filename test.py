import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
couleurs = {"Couleur":"rouge","Animal":"Chien", "Nombre":23}
 
print(get_close_matches("anim",couleurs.keys()))
