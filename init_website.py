import csv
import os
import aw

def creer_dict_poke(fichier):
    dico_global = {}

    with open(fichier, encoding="utf-8", newline='') as csvfile:
        BDD = csv.DictReader(csvfile)
        for ligne in BDD:
            id_poke = ligne["Pokemon Id"]
            dico_global[id_poke] = ligne

    return dico_global

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
    
def reset_fichier(Nom_Fichier, Nom_Dossier = None):
    if Nom_Dossier != None:
        Nom_Fichier = Nom_Dossier + '/' + Nom_Fichier
    file = open(Nom_Fichier, "w")
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
    for e in dico:
        ecrire_fichier(f'{e['Pokemon Name']}.html','templates/pokedex',f'Page de {e["Pokemon Name"]}')
        Page_flask = (("modeles/main_page_flask.txt".read()).replace('%page%', e['Pokemon Name'])).replace('%_emplacement_%', f"templates/pokedex/{e["Pokemon Name"]}")
        ecrire_fichier('main.py', Page_flask)
    ecrire_fichier("main.py", 'modeles/main_fin.txt')
    return
        
        
        
        

if __name__ == '__main__':
    dico_pke = creer_dict_poke('Pkm_dbse.csv')
    print('Dico créé')
    print(dico_pke['1800'])
    creer_dossier('templates')
    creer_dossier("Teams", 'templates')
    ecrire_fichier('main.py', None, lire_fichier('main.txt'))
    
    creer_main(dico_pke)
    

    
    
    
