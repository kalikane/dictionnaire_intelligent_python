import json
from safeprint import print
import difflib #est une librerie pour comparer les textes
from difflib import SequenceMatcher
from difflib import get_close_matches
import cv2 

#on ouvre le fichier data.json avec la methode open
data = json.load(open("data.json"))


#fonction qui va chercher la definition d'un mot
def Translate(w):
    w =  w.lower()

    #On verifie si le mot demander par l'utilisateur est dans le fichier l
    if w in data :
        #On retourne la valeur du mot. le mot etant la clé
        return data[w]

        #on met la premiere lettre du mot en majiscule avec la 
        #la fonction Title avant de faire la recherche
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]

        #get_close_matches est en faite une fonction de la librairie 
        #difflib qui va calculer le pourcentage de ressemblace entre
        #entre se que l'utilisateur entre et tout les mot du fichier 
        #json
    elif len(get_close_matches(w, data.keys()) ) > 0:

        #On pren la premier valeur car la fontion get_close_matches
        #retourne une liste de valeur
        yn = input("you want to say %s instead ? Enter Y if yes or N if No : " % get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
           return data[get_close_matches(w,data.keys())[0]]
        elif  yn == "n":
            return " Sorry this word doesn't exist."
        else:
            return "i didn't understand your entry."
    else :
         return " Sorry this word doesn't exist."

word = input("Enter the word : ")
output = Translate(word)
if type (output) == list:
   for item in output:
       print(item)
else :
    print(Translate(word))

