import csv
import os
import aw
import sys
import time
# coding: iso-8859-1 -*-
def creer_dict_poke(fichier):
    dico_global = {}

    with open(fichier, encoding="utf-8", newline='') as csvfile:
        BDD = csv.DictReader(csvfile)
        for ligne in BDD:
            id_poke = ligne["Pokemon Id"]
            dico_global[id_poke] = ligne
            if (ligne['Alternate Form Name']) != "NULL":
                dico_global[id_poke]['Pokemon Name'] = ligne['Pokemon Name'][:-1]+ligne['Alternate Form Name'][1:]
                print(dico_global[id_poke]['Pokemon Name'])
            dico_global[id_poke]["Pokemon Name"] = formatage(dico_global[id_poke]["Pokemon Name"])           
    return dico_global

def formatage(mot):
    Nf = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', "'", ' (', ')', ". ", '-', ' ', '.',':','?','!',"%"]
    F = ["e", "e", "e", "a", "u", "u", "c", "o", "i", "i", "a", "", "_","", "", "", "", "", "","Question_Mark", "Exclamation_Mark","Pct"]
    for i in range(len(Nf)):
        mot = mot.replace(Nf[i], F[i])
    return mot



def creer_dossier(Nom_Dossier, Emplacement = None):
    if Emplacement != None:
        Nom_Dossier = Emplacement + '/' + Nom_Dossier
    try:
        os.mkdir(Nom_Dossier)
        print(f"Dossier {Nom_Dossier} crée.")
        return
    except OSError as e:
        if e.errno == 17:
            print(f"Dossier {Nom_Dossier} déjà existant.")
        
def ecrire_fichier(Nom_Fichier, Nom_Dossier = None, Content = None):
    if Nom_Dossier != None:
        Nom_Fichier = Nom_Dossier + '/' + Nom_Fichier
    file = open(Nom_Fichier, "a")
    file.write(Content)
    file.close()
    
def lire_fichier(Nom_Fichier):
    f = open(Nom_Fichier)
    contenu = f.read()
    f.close
    return contenu        

def creer_main(dico):
    ecrire_fichier('main.py', None, lire_fichier('modeles/main_debut.txt'))
    creer_dossier('templates')
    creer_dossier('pokedex', 'templates')
    creer_dossier('static')
    for e in dico.values():
        print(e)
        ecrire_fichier(f'{e['Pokemon Name'][1:-1]}.html','templates/pokedex',f'Page de {e["Pokemon Name"]}')
        Mod_page = open("modeles/main_page_flask.txt", 'r')
        Page_flask = Mod_page.read()
        Page_flask = Page_flask.replace('%page%', e['Pokemon Name'][1:-1])
        Page_flask = Page_flask.replace('%_emplacement_%', f"/pokedex/{e["Pokemon Name"][1:-1]}")
        print(Page_flask)
        Mod_page.close()
        ecrire_fichier('main.py',None, Page_flask)
    ecrire_fichier("main.py",None, lire_fichier('modeles/main_fin.txt'))
    return
        
        
        
        

if __name__ == '__main__':
    a = time.time()
    # Reset des fichiers modifiés
    try:
        os.removedirs("/templates")
    except:
        print("Dossier non existant.")
        
    try:
        os.remove("main.py")
    except:
        print("Fichier non trouvé")
    
    while(time.time()-a < 5):
        continue
    
    dico_pke = creer_dict_poke('Pkm_dbse.csv')
    print('Dico créé')
    print(dico_pke['1800'])
    creer_dossier('templates')
    creer_dossier("Teams", 'templates')
    
    creer_main(dico_pke)
    print('succès !')

    
    
    
