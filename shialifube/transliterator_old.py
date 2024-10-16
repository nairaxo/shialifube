# shialifube/transliterator_old.py

from shialifube.data import unigrams_lat, digrams_lat, unigrams_ara, digrams_ara

def detect_hamza(chaine):
    chaine = chaine.split(" ")
    for i in range(len(chaine)):
        chaine[i] = list(chaine[i])
        for j in range(len(chaine[i])):
            if j != 0 and j != len(chaine[i]) and chaine[i][j] == "ا":             
                chaine[i][j] = "ا"
        chaine[i] = "".join(chaine[i])
    return " ".join(chaine)

def latin_to_arabic(chaine):
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




def detect_language(word):
    count_lat = 0
    count_ara = 0
    for i in range(len(word)):
        if word[i] in list(unigrams_lat.keys()):
            count_lat += 1
        elif word[i] in list(unigrams_ara.keys()):
            count_ara += 1
    if count_lat > count_ara:
        return "latin"
    elif count_ara > count_lat:
        return "arabic"
    return "unknown"

def arabic_to_latin(chaine):
    ## gestion des "e"
    

def transliterate(chaine):
    chaine = str(chaine).split(" ")
    count_lat = 0
    count_ara = 0   
    for i in range(len(chaine)):
        lang = detect_language(chaine[i])
        if lang == "latin":
            count_lat += 1
        elif lang == "arabic":
            count_ara += 1

    chaine = " ".join(chaine)
    if count_lat > count_ara:
        return latin_to_arabic(chaine)
    # elif count_ara > count_lat:
    #     return arabic_to_latin(chaine)
    # else:
    #     return arabic_to_latin(chaine)

# text = "ل‍ہ‍وه ووسيكو muhimu halisi"
text = "lawa yapvo"
text = "لو يڢه"

text = "مونده"

text = "nga ni hwandzo"

text = "نڠﺍ ني حوﺍنزّه"

text = "ndami nawe rimana"

text = "ندﺍمي نﺍو‍ہ‍ ريمﺍنﺍ"

text = "yinu ya hangu"

text = "ينو يﺍ حﺍنڠو"

trans = transliterate(text)
print(trans)
with open("trans2.txt", "w", encoding="utf-8") as f:
    f.write(trans)