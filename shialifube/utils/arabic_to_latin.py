from shialifube.data import unigrams_lat, digrams_lat, unigrams_ara, digrams_ara

def transliterate(chaine):
    ## replace the digrams
    for digram in digrams_ara.keys():
        chaine = chaine.replace(digram, digrams_ara[digram]["lat"])
    
    ## gérer les "\u200dہ\u200d"
    if "‍ہ‍" in chaine:
        chaine = chaine.replace("‍ہ‍", "e")

    ## segmenter la chaîne en caractères
    chaine = list(chaine)

    for i in range(len(chaine)):
        ## traiter uniquement les caractères non latins
        if chaine[i] not in unigrams_lat.keys() and chaine[i] not in digrams_lat.keys():
            ## gestion des "و" et "u"
            if chaine[i] == "و":
                # if i == len(chaine)-1:
                if i != 0:
                    chaine[i] = "u"
                else:
                    chaine[i] = "w"
            ## gestion des "ي", "i" et "y"
            elif chaine[i] == "ي":
                if i == 0 and len(chaine) > 1 and chaine[i+1] == "ﺍ":
                    chaine[i] = "y"
                elif i < len(chaine)-1 and chaine[i+1] == "ي":
                    chaine[i] = "i"
                    chaine[i+1] = "y"
                else:
                    chaine[i] = "i"
            else:
                ## default
                chaine[i] = unigrams_ara[chaine[i]]["lat"]

    chaine = "".join(chaine)
    return chaine
