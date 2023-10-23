from datetime import datetime


def convertir_date_en_lettres(date_str):
    # Convertir la date en objet datetime
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')

    # Dictionnaire pour les mois
    mois = {
        1: 'janvier', 2: 'février', 3: 'mars', 4: 'avril',
        5: 'mai', 6: 'juin', 7: 'juillet', 8: 'août',
        9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'décembre'
    }
     # Dictionnaire pour les chiffres de 1 à 31
    chiffres_1_31 = {
        1: 'premier', 2: 'deux', 3: 'trois', 4: 'quatre', 5: 'cinq',
        6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf', 10: 'dix',
        11: 'onze', 12: 'douze', 13: 'treize', 14: 'quatorze', 15: 'quinze',
        16: 'seize', 17: 'dix-sept', 18: 'dix-huit', 19: 'dix-neuf', 20: 'vingt',
        21: 'vingt et un', 22: 'vingt-deux', 23: 'vingt-trois', 24: 'vingt-quatre',
        25: 'vingt-cinq', 26: 'vingt-six', 27: 'vingt-sept', 28: 'vingt-huit',
        29: 'vingt-neuf', 30: 'trente', 31: 'trente et un'
    }
    
    nombres = {
    23: 'vingt-trois',
    24: 'vingt-quatre',
    25: 'vingt-cinq',
    26: 'vingt-six',
    27: 'vingt-sept',
    28: 'vingt-huit',
    29: 'vingt-neuf',
    30: 'trente',
    31: 'trente et un',
    32: 'trente-deux',
    33: 'trente-trois',
    34: 'trente-quatre',
    35: 'trente-cinq',
    36: 'trente-six',
    37: 'trente-sept',
    38: 'trente-huit',
    39: 'trente-neuf',
    40: 'quarante',
    41: 'quarante et un',
    42: 'quarante-deux',
    43: 'quarante-trois',
    44: 'quarante-quatre',
    45: 'quarante-cinq',
    46: 'quarante-six',
    47: 'quarante-sept',
    48: 'quarante-huit',
    49: 'quarante-neuf',
    50: 'cinquante'
}
    # Convertir l'année en lettres
    a=date_obj.year - 2000
    annee_en_lettres = f"deux mille { nombres[a] }"
#`hhhhhhhhh jj ${nombres} yyyyyy `
    # Convertir le mois en lettres
    mois_en_lettres = mois[date_obj.month]

    # Convertir le jour en lettres
    jour_en_lettres = chiffres_1_31[date_obj.day]

    # Formater la date en lettres
    date_en_lettres = f"l'an {annee_en_lettres} et le {jour_en_lettres} {mois_en_lettres} "

    return date_en_lettres



# Exemple d'utilisation
date_a_convertir = "20/12/2030"
resultat_date = convertir_date_en_lettres(date_a_convertir)
print(f"{date_a_convertir} en lettres : {resultat_date}")









