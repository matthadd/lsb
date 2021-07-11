# CHIFFREMENT PAR  INVERSE MODULAIRE

def chiffrer(lettre_a_chiffrer):
    # Etape 1 : Créer le dictionnaire
    d = dict()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        d[alphabet[i]] = i
    chiffre = d[lettre_a_chiffrer]

    # Etape 2 :  Formule de chiffrement
    lettre_chiffree = (11 * chiffre + 8) % 26

    # Etape 3 : Inverser le dictionnaire et renvoyer la lettre codée
    d = {v: k for k, v in d.items()}
    lettre_codee = d[lettre_chiffree]

    return lettre_codee


def dechiffrer(lettre_a_dechiffrer):
    # Etape 1 : Créer le dictionnaire
    d = dict()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        d[alphabet[i]] = i
    chiffre = d[lettre_a_dechiffrer]

    # Etape 2 :  Formule de chiffrement
    lettre_dechiffree = (19 * chiffre + 4) % 26

    # Etape 3 : Inverser le dictionnaire et renvoyer la lettre codée
    d = {v: k for k, v in d.items()}
    lettre_decodee = d[lettre_dechiffree]

    return lettre_decodee


lettre_a_chiffrer = "m"
lettre_codee = chiffrer(lettre_a_chiffrer)
print(lettre_codee)


def chiffrer_mot(mot_a_chiffrer):
    resultat = ""
    for i in range(len(mot_a_chiffrer)):
        resultat += chiffrer(mot_a_chiffrer[i])
    return resultat


mot = "maths"
print(chiffrer_mot(mot))


def dechiffrer_mot(mot_a_dechiffrer):
    resultat = ""
    for i in range(len(mot_a_dechiffrer)):
        resultat += dechiffrer(mot_a_dechiffrer[i])
    return resultat


mot2 = "taxgujajsavva"
print(dechiffrer_mot(mot2))

mot_a_chiffrer = "singe"
print(mot_a_chiffrer)
mot_chiffrer = chiffrer_mot(mot_a_chiffrer)
print(mot_chiffrer)
mot_dechiffrer = dechiffrer_mot(mot_chiffrer)
print(mot_dechiffrer)
