# shialifube/transliterator.py

unigrams = {
    'a': {'ara': 'ﺍ', 'phon': '/a/'},
    'ɓ': {'ara': 'ﺏ', 'phon': '/ɓ/'},
    'b': {'ara': 'ب', 'phon': '/b/'},
    'c': {'ara': 'شّ', 'phon': '/t͡ʃ/'},
    'ɗ': {'ara': 'د', 'phon': '/ɗ/'},
    'd': {'ara': 'د', 'phon': '/d/'},
    'e': {'ara': '\u200dہ\u200d', 'phon': '/e/'},
    'f': {'ara': 'ف', 'phon': '/f/'},
    'g': {'ara': 'غ', 'phon': '/g/'},
    'h': {'ara': 'ح', 'phon': '/h/'},
    'i': {'ara': 'ي', 'phon': '/i/'},
    'j': {'ara': 'ج', 'phon': '/d͡ʒ/'},
    'k': {'ara': 'ك', 'phon': '/k/'},
    'l': {'ara': 'ل', 'phon': '/l/'},
    'm': {'ara': 'م', 'phon': '/m/'},
    'n': {'ara': 'ن', 'phon': '/n/'},
    'o': {'ara': 'ه', 'phon': '/o/'},
    'p': {'ara': 'پ', 'phon': '/p/'},
    'r': {'ara': 'ر', 'phon': '/r/'},
    's': {'ara': 'س', 'phon': '/s/'},
    't': {'ara': 'ﺕ', 'phon': '/t/'},
    'u': {'ara': 'و', 'phon': '/u/'},
    'v': {'ara': 'ڤ', 'phon': '/v/'},
    'w': {'ara': 'و', 'phon': '/w/'},
    'y': {'ara': 'ي', 'phon': '/j/'},
    'z': {'ara': 'ز', 'phon': '/z/'},
    ' ': {'ara': ' ', 'phon': ' '}
}

digrams = {
    "dh" : {"ara" : "ذ", "phon" : "/ð/"},
    "dj" : {"ara" : "ج", "phon" : "/d͡ʒ/"},
    "dr" : {"ara" : "رّ", "phon" : "/ɖ/"},
    "dz" : {"ara" : "زّ", "phon" : "/d͡z/"},
    "gh" : {"ara" : "غ", "phon" : "/ɣ/"},
    "ny" : {"ara" : "نّ", "phon" : "/ɲ/"},
    "sh" : {"ara" : "ش", "phon" : "/ʃ/"},
    "pv" : {"ara" : "ڢ", "phon" : "/β/"},
    "th" : {"ara" : "ث", "phon" : "/θ/"},
    "tr" : {"ara" : "تّ", "phon" : "/ʈ/"},
    "ts" : {"ara" : "سّ", "phon" : "/t͡s/"}
}


def detect_hamza(chaine):
    chaine = chaine.split(" ")
    for i in range(len(chaine)):
        chaine[i] = list(chaine[i])
        for j in range(len(chaine[i])):
            if j != 0 and j != len(chaine[i]) and chaine[i][j] == "ﺍ":                
                chaine[i][j] = ""
        chaine[i] = "".join(chaine[i])
    return " ".join(chaine)

def transliterate(chaine):
    lst_bigrams = [chaine[i:i+2] for i in range(len(chaine) - 1)]
    lst_bigrams2 = []
    for elem in lst_bigrams:
        if elem in list(digrams.keys()):
            lst_bigrams2.append(elem)

    for digram in lst_bigrams2:
        chaine = chaine.replace(digram, digrams[digram]["ara"])
    for i in range(len(chaine)):
        # if chaine[i] == "a":

        try:
            chaine = chaine.replace(chaine[i], unigrams[chaine[i]]["ara"])
        except:
            continue

    chaine = detect_hamza(chaine)
    chaine = list(chaine)
    for i in range(len(chaine)):
        try:
            chaine[i] = unigrams[chaine[i]]["ara"]
        except:
            continue
    chaine = "".join(chaine)
    return chaine

