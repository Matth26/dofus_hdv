#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sikuli import *
from time import sleep

from datetime import datetime


#Variables globales


#menuGauche contient tout les 12 lignes du menu gauche, vignette exclue
rMenuGauche = Region(1902,396,516,541)

#menuGx contient la ligne x vignette exclue de haut en bas
rMenuG1 = Region(1901,395,508,44)
rMenuG2 = Region(1904,443,510,39)
rMenuG3 = Region(1903,488,515,44)
rMenuG4 = Region(1904,533,507,41)
rMenuG5 = Region(1903,577,512,42)
rMenuG6 = Region(1902,623,507,43)
rMenuG7 = Region(1905,668,511,41)
rMenuG8 = Region(1903,711,507,47)
rMenuG9 = Region(1903,758,507,39)
rMenuG10 = Region(1901,805,514,39)
rMenuG11 = Region(1900,851,511,40)
rMenuG12 = Region(1903,893,511,42)
rMenuGListe = [rMenuG1,rMenuG2,rMenuG3,rMenuG4,rMenuG5,rMenuG6,rMenuG7,rMenuG8,rMenuG9,rMenuG10,rMenuG11,rMenuG12]
#objet pris sur le menu déroulant gauche
rCat = Region(2035,331,331,38)

#Menu déroulant des catégories de haut en bas, à prendre sur l hdv ressource
rCat1 = Region(2043,374,329,41)
rCat2 = Region(2046,414,325,44)
rCat3 = Region(2043,471,331,33)
rCat4 = Region(2043,514,336,34)
rCat5 = Region(2041,561,333,30)
rCat6 = Region(2043,606,313,34)
rCat7 = Region(2043,652,306,28)
rCat8 = Region(2041,698,318,27)
rCat9 = Region(2043,745,316,25)
rCat10 =Region(2042,790,321,27)
rCatListe = [rCat1,rCat2,rCat3,rCat4,rCat5,rCat6,rCat7,rCat8,rCat9,rCat10]

#menuDroit  contient tout les ligne du menu droit de haut en bas
rMenuDroit = Region(2498,701,848,224)
rMenuD11=Region(2548,704,194,37)
rMenuD12=Region(2747,703,186,41)
rMenuD13=Region(2944,706,186,35)
rMenuD21=Region(2549,748,191,45)
rMenuD22=Region(2747,748,188,43)
rMenuD23=Region(2942,749,189,41)
rMenuD31=Region(2549,796,187,35)
rMenuD32= Region(2748,794,189,38)
rMenuD33=Region(2943,797,187,36)
rMenuD41=Region(2552,840,187,39)
rMenuD42=Region(2746,837,188,43)
rMenuD43=Region(2943,840,188,37)
rMenuD51=Region(2550,885,189,39)
rMenuD52=Region(2748,885,186,39)
rMenuD53=Region(2943,885,187,41)
rMenuDMatrice = [[rMenuD11, rMenuD12, rMenuD13], [rMenuD21, rMenuD22, rMenuD23], [rMenuD31, rMenuD32, rMenuD33], [rMenuD41, rMenuD42, rMenuD43], [rMenuD51, rMenuD52, rMenuD53]]



#prixMoyen contient tout la ligne du prix moyen
rPrixMoyen = Region(2990,935,343,43)

#niveau pris en haut a droite une fois une des piles cliquée préfixée par niv.
rNiv = Region(3162,261,184,45)


#cartouche Pos menu déroulant
rCartouchePosG = Region(2416,396,27,542)
rCartouchePosD = Region(3321,702,24,223)



def testRegions (l):
    for r in l:
        mouseMove (r)
        




def ecrireFichier(contenu,nomFichier):
    x = getBundleFolder()
    #print(x)
    #print(contenu)
    with open(x + nomFichier, "a") as myfile:
        myfile.write(contenu)
    
# Return True si on est la en bat du chariot
def scroll2(cartouchePos,wheelDir):
    mouseMove(cartouchePos)
    prev = capture(cartouchePos)
    wheel(wheelDir, 1)
    sleep(0.1)
    try:
        return (cartouchePos.find(prev).getScore() > 0.99)
    except:
        return False
    
def scrollToutEnHaut(cartouchePos):
    i = 0
    while(not(scroll2(cartouchePos,WHEEL_UP))):
        i = i + 1

def scrollToutEnBas(cartouchePos):
    i = 0
    while(not(scroll2(cartouchePos,WHEEL_DOWN))):
        i = i + 1
#x=Region(1900,396,516,540)
#print (x.text())
#click(capture(x).find("Capignon"))
#print(finScroll())

def litMenuDroiteRess(region) :
    click(region)
    sleep(0.1)
    j = 0
    while j < 2 and not (rMenuDMatrice[0][j].text()):
        print j
        j = j+1
    click (rMenuDMatrice[0][j])
    mouseMove(rCartouchePosD)
    nom = region.text()
    niveau = rNiv.text()[4:]
    now = datetime.now()
    date = now.strftime(";%m;%d;%Y;%H;%M;%S;")
    res = nom + ";" + rCat.text() + ";" + niveau + date + ";" + rPrixMoyen.text() + ";" + rMenuD11.text() + ";" + rMenuD12.text() + ";" + rMenuD13.text() + "\n"
    ecrireFichier(res,"scanRessource.csv")
    return res


def litMenuDroiteItem(region) :
    click(region)
    scrollToutEnHaut(rCartouchePosD)
    click(rMenuD11)
    mouseMove(rCartouchePosD)
    nom = region.text()
    niveau = rNiv.text()[4:]
    now = datetime.now()
    date = now.strftime(";%m;%d;%Y;%H;%M;%S;")
    res = nom + ";" + rCat.text() + ";" + niveau + date + ";" + rPrixMoyen.text() + ";"
    # On lit les 5 premiers
    i = 0
    while i<5:
        res = res + rMenuDMatrice[i][0].text() + ";"
        i = i + 1
    # On scroll/lit jusqu à la fin 3 par 3, potentiellement des doublons à la fin
    while(not(scroll2(rCartouchePosD,WHEEL_DOWN))):
        i = 2
        while i<5:
            res = res + rMenuDMatrice[i][0].text() + ";"
            i = i + 1
    res = res + "\n"
    ecrireFichier(res,"scanRessource.csv")
    return res
    


def litMenuGauche(callback):
    click(rMenuG1)
    scrollToutEnHaut(rCartouchePosG)
    res = ""
    #On lit les 3 premiers
    i = 0
    while (i < 3):
        res = res + callback(rMenuGListe[i])
        i = i + 1
        
    #On scroll, à chaque itération, on lit les 3 premiers    
    i=0
    while(not(scroll2(rCartouchePosG,WHEEL_DOWN))):
        i = 0
        while (i < 3):
           res = res + callback(rMenuGListe[i])
           i = i + 1
    #On a fini, on lit les 7 derniers
    i = 3
    while (i < 12):
        res = res + callback(rMenuGListe[i])  
        i = i + 1
    return res    

def litMenuCat (nbCat , typeHdv):
    callback = litMenuDroiteItem
    if typeHdv == "ress":
        callback = litMenuDroiteRess
    res = ""
    i=0
    #lit le début
    while((i < nbCat) and (i < 10)):
        click(rCat)
        click(rCatListe[i])
        res = res + litMenuGauche(callback)
        i = i + 1
    #scroll et lit jusqu à al fin (potentiellement on lit deux fois les derniers)
    nbScroll = 1 
    while ( i < nbCat):
        click(rCat)
        mouseMove(rCat1)
        wheel(WHEEL_DOWN, nbScroll)
        click(rCat8)
        res = res + litMenuGauche(callback)
        click(rCat)
        mouseMove(rCat1)
        wheel(WHEEL_DOWN, nbScroll)
        click(rCat9)
        res = res + litMenuGauche(callback)
        click(rCat)
        mouseMove(rCat1)
        wheel(WHEEL_DOWN, nbScroll)
        click(rCat10)
        res = res + litMenuGauche(callback)
        nbScroll = nbScroll + 1
        i = i+3 
    pos = i
    if i > nbCat: 
        pos = i - 3
    j=0
    while(pos+j<nbCat):
        rCurr = rCatListe[9-j]
        click(rCat)
        mouseMove(rCat1)
        wheel(WHEEL_DOWN, nbScroll)
        click(rCurr)
        res = res + litMenuGauche(callback)
        j = j + 1
    return res


#litMenuCat(5,"ress")

