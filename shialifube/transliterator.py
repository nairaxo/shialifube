# shialifube/transliterator.py

from shialifube.data import unigrams_lat, digrams_lat, unigrams_ara, digrams_ara

def arabic_latin(chaine):
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
                if i < len(chaine)-1 and chaine[i+1] == "ﺍ":
                    chaine[i] = "w"
                elif i != 0:
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
                elif i == 0:
                    chaine[i] = "y"
                else:
                    chaine[i] = "i"
            else:
                ## default
                chaine[i] = unigrams_ara[chaine[i]]["lat"]

    chaine = "".join(chaine)
    return chaine

def detect_hamza(chaine):
    chaine = chaine.split(" ")
    for i in range(len(chaine)):
        chaine[i] = list(chaine[i])
        for j in range(len(chaine[i])):
            if j != 0 and j != len(chaine[i]) and chaine[i][j] == "ا":             
                chaine[i][j] = "ا"
        chaine[i] = "".join(chaine[i])
    return " ".join(chaine)

def latin_arabic(chaine):
    lst_bigrams = [chaine[i:i+2] for i in range(len(chaine) - 1)]
    lst_bigrams2 = []
    for elem in lst_bigrams:
        if elem in list(digrams_lat.keys()):
            lst_bigrams2.append(elem)

    for digram in lst_bigrams2:
        chaine = chaine.replace(digram, digrams_lat[digram]["ara"])
    for i in range(len(chaine)):
        # print(chaine[i])
        # if chaine[i] == "a" and i != 0 and i != len(chaine) - 1: #and chaine[i - 1] == "h" and chaine[i + 1] == "h":
        #     chaine = chaine.replace(chaine[i], "ﺍ")
    
        try:
            chaine = chaine.replace(chaine[i], unigrams_lat[chaine[i]]["ara"])
        except:
            continue

    chaine = detect_hamza(chaine)
    chaine = list(chaine)
    for i in range(len(chaine)):
        try:
            chaine[i] = unigrams_lat[chaine[i]]["ara"]
        except:
            continue
    chaine = "".join(chaine)
    return chaine


def transliterate(text):
    ## detect the language
    count_lat = 0
    count_ara = 0
    for letter in text:
        if letter in unigrams_lat.keys():
            count_lat += 1
        if letter in unigrams_ara.keys():
            count_ara += 1
    if count_lat > count_ara:
        lang = "latin"
    elif count_ara > count_lat:
        lang = "arabic"
    else:
        lang = "latin"

    if lang == "arabic":
        trans = arabic_latin(text)
    else:
        trans = latin_arabic(text)

    return trans

