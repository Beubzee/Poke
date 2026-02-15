def formatage(mot):
    '''
    Remplace les caractères indésirables pour la création des pages individuelles dans main.py.
    '''
    Nf = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', "'", ' (', ')', ". ", '-', ' ', '.',':','?','!',"%"]
    F = ["e", "e", "e", "a", "u", "u", "c", "o", "i", "i", "a", "", "_","", "", "", "", "", "","Question_Mark", "Exclamation_Mark","Pct"]
    for i in range(len(Nf)):
        mot = mot.replace(Nf[i], F[i])
    return mot

def formatage_txt(mot):
    '''
    Remplace les caractères indésirables pour la création des pages individuelles dans main.py.
    '''
    Nf = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    F = ["e", "e", "e", "a", "u", "u", "c", "o", "i", "i", "a"]
    for i in range(len(Nf)):
        mot = mot.replace(Nf[i], F[i])
    return mot