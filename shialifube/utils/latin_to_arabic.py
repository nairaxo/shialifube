from shialifube.data import unigrams_lat, digrams_lat

def detect_hamza(chaine):
    chaine = chaine.split(" ")
    for i in range(len(chaine)):
        chaine[i] = list(chaine[i])
        for j in range(len(chaine[i])):
            if j != 0 and j != len(chaine[i]) and chaine[i][j] == "ا":             
                chaine[i][j] = "ا"
        chaine[i] = "".join(chaine[i])
    return " ".join(chaine)

def transliterate(chaine):
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


text = "linu ɗaɓa eka hakiri"
trans = transliterate(text)
print(trans)