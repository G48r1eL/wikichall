import bs4
import requests
import os

def clear(): os.system('cls')
clear()
PageOHasard = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"

def objectife():
        reponse = requests.get(PageOHasard)
        soup = bs4.BeautifulSoup(reponse.text, 'html.parser')
        return soup.title.string
objectif=objectife()
def liste_liens(url):
    tableLiens = []
    tableTitre = []
    i = 0
    reponse = requests.get(url)
    soup = bs4.BeautifulSoup(reponse.text, 'html.parser')
    title = soup.title.string
    soup = soup.find("main", {"class": "mw-body"})
    print("OBJECTIF : "+ objectif)
    for liens in soup.find_all('a'):
        lien = liens.get('href')
        titre = liens.get('title')
        if titre != None and "Modifier la section" not in titre:
            print(str(i) +'/'+ titre)
            tableLiens.append(lien)
            tableTitre.append(titre)
            i += 1
    Choice = input()
    return tableLiens[int(Choice)],title;
def wiki_game():
    global objectif
    while 1==1:
        print("Bienvenue dans le Wikipédia Challenge")
        print("1 : Commencer / 2 : Changer objectif")
        print("OBJECTIF : "+ objectif)
        choixmenu = input()
        clear()
        if choixmenu == "1":
            break
        elif choixmenu == "2":
             objectif = objectife()
        else:
            print("Entrée invalide")
        
    link , title = liste_liens(PageOHasard)
    while 1==1:
        clear()
        link,title =liste_liens("https://fr.wikipedia.org"+link) 
        print(str(title)+str(objectif))
        if str(title) == str(objectif):
            print("Bravo tu as Gagné")
            break 

wiki_game()