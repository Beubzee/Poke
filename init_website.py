import csv, os, aw, sys, time
from fonctions import *

def lprint(*Elements, end = '\n'): # Le caractère * Permet d'accepter un nombre infini de paramètres
    file = open("logs/log_init_website.txt", 'a')
    print(Elements, end = end)
    file.write(f'{Elements}'[2:-3]+'\n')
    file.close()
    return   
    

def creer_dict_poke(fichier):
    dico_global = {}

    with open(fichier, encoding="utf-8", newline='') as csvfile:
        BDD = csv.DictReader(csvfile)
        for ligne in BDD:
            id_poke = ligne["Pokemon Id"]
            dico_global[id_poke] = ligne
            for e in ligne.keys():
                
                ligne[e] = formatage_txt(ligne[e])
                
            if (ligne['Alternate Form Name']) != "NULL":
                dico_global[id_poke]['Pokemon Name'] = ligne['Pokemon Name'][:-1]+ligne['Alternate Form Name'][1:]
                lprint(dico_global[id_poke]['Pokemon Name'])
            dico_global[id_poke]["Pokemon Name"] = formatage(dico_global[id_poke]["Pokemon Name"])           
    return dico_global

def creer_dossier(Nom_Dossier, Emplacement = None):
    if Emplacement != None:
        Nom_Dossier = Emplacement + '/' + Nom_Dossier
    try:
        os.mkdir(Nom_Dossier)
        lprint(f"Dossier {Nom_Dossier} crée.")
        return
    except OSError as e:
        if e.errno == 17:
            lprint(f"Dossier {Nom_Dossier} déjà existant.")
        
def ecrire_fichier(Nom_Fichier, Nom_Dossier = None, Content = None, mode_ecriture = 'a'):
    if Nom_Dossier != None:
        Nom_Fichier = Nom_Dossier + '/' + Nom_Fichier
    file = open(Nom_Fichier, mode_ecriture)
    file.write(Content)
    file.close()
    
def lire_fichier(Nom_Fichier):
    with open(Nom_Fichier) as f:
        return f.read()
      

def creer_main(dico):
    ecrire_fichier('main.py', None, lire_fichier('modeles/main_debut.txt'))
    creer_dossier('templates')
    creer_dossier('pokedex', 'templates')
    creer_dossier('static')
    for e in dico.values():
        creer_page_poke(e)
    ecrire_fichier("main.py",None, lire_fichier('modeles/main_fin.txt'))
    return
        
def creer_page_poke(e):
    lprint(e)
    creer_html_poke(e)
    Mod_page = open("modeles/main_page_flask.txt", 'r')
    Page_flask = Mod_page.read()
    Page_flask = Page_flask.replace('%page%', e['Pokemon Name'][1:-1])
    Page_flask = Page_flask.replace('%_emplacement_%', f"/pokedex/{e['Pokemon Name'][1:-1]}")
    lprint(Page_flask)
    Mod_page.close()
    ecrire_fichier('main.py',None, Page_flask)
        
def creer_html_poke(e):         # Creation du fichier html en remplacant les paramètres du modèle par les donnees du poke
    Template = lire_fichier("modeles/html.txt")
    Donnees_html = ['%Pokemon ID%', '%Pokedex Number%', '%Pokemon Name%', '%Classification%', '%Alternate Form Name%', '%Original Pokemon ID%', '%Legendary Type%', '%Pokemon Height%', '%Pokemon Weight%', '%Primary Type%', '%Secondary Type%', '%Primary Ability%', '%Primary Ability Description%', '%Secondary Ability%', '%Secondary Ability Description%', '%Hidden Ability%', '%Hidden Ability Description%', '%Special Event Ability%', '%Special Event Ability Description%', '%Male Ratio%', '%Female Ratio%', '%Base Happiness%', '%Game(s) of Origin%', '%Health Stat%', '%Attack Stat%', '%Defense Stat%', '%Special Attack Stat%', '%Special Defense Stat%', '%Speed Stat%', '%Base Stat Total%', '%Health EV%', '%Attack EV%', '%Defense EV%', '%Special Attack EV%', '%Special Defense EV%', '%Speed EV%', '%EV Yield Total%', '%Catch Rate%', '%Experience Growth%', '%Experience Growth Total%', '%Primary Egg Group%', '%Secondary Egg Group%', '%Egg Cycle Count%', '%Pre-Evolution Pokemon Id%', '%Evolution Details%']
    Donnees_remplacees = [e['Pokemon Id'], e['Pokedex Number'], e['Pokemon Name'], e['Classification'], e['Alternate Form Name'], e['Original Pokemon ID'], e['Legendary Type'], e['Pokemon Height'], e['Pokemon Weight'], e['Primary Type'], e['Secondary Type'], e['Primary Ability'], e['Primary Ability Description'], e['Secondary Ability'], e['Secondary Ability Description'], e['Hidden Ability'], e['Hidden Ability Description'], e['Special Event Ability'], e['Special Event Ability Description'], e['Male Ratio'], e['Female Ratio'], e['Base Happiness'], e['Game(s) of Origin'], e['Health Stat'], e['Attack Stat'], e['Defense Stat'], e['Special Attack Stat'], e['Special Defense Stat'], e['Speed Stat'], e['Base Stat Total'], e['Health EV'], e['Attack EV'], e['Defense EV'], e['Special Attack EV'], e['Special Defense EV'], e['Speed EV'], e['EV Yield Total'], e['Catch Rate'], e['Experience Growth'], e['Experience Growth Total'], e['Primary Egg Group'], e['Secondary Egg Group'], e['Egg Cycle Count'], e['Pre-Evolution Pokemon Id'], e['Evolution Details']]
    Mod_page = open("modeles/html.txt", 'r')
    Page = Mod_page.read()
    for i in range(len(Donnees_html)):
        Donnees_remplacees[i] = Donnees_remplacees[i].replace("'", '')
        Donnees_remplacees[i] = Donnees_remplacees[i].replace('"', '')
            
        Page = Page.replace(Donnees_html[i], Donnees_remplacees[i])
    Page = Page.replace("__data__", f'{e}')
    ecrire_fichier(f"{e['Pokemon Name'][1:-1]}.html", 'templates/pokedex', Page, 'w')

def initialiser_pages_poke(): # On l'appellera dans le main, en faire une fonction permet de l'appeler depuis un autre fichier
    # Reset des fichiers modifiés
    try:
        os.removedirs("templates")
    except:
        lprint("Dossier non existant.")
        
    try:
        os.remove("main.py")
    except:
        lprint("Fichier non trouvé")

    
    dico_pke = creer_dict_poke('Pkm_dbse.csv')
    lprint('Dico créé')
    lprint(dico_pke['1800'])
    creer_dossier('templates')
    
    creer_main(dico_pke)
    lprint('succès !')
    
    lprint(dico_pke.keys())
    
    a = dico_pke['1']
    for e in a.keys():
        lprint(f"'%{e}%'", end = ', ')    

if __name__ == '__main__':
    try:
        os.remove("logs/log_init_website.txt")
    except:
        lprint("Fichier non trouvé")
    initialiser_pages_poke()