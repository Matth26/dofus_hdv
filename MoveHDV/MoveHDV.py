#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sikuli import *
from time import sleep

#Variables globales

#Regions dans le menu du Zaapi
rMenuZaapi1 = Region(2170,369,564,52)
rMenuZaapi2 = Region(2170,425,562,49)
rMenuZaapi3 = Region(2172,481,538,52)
rMenuZaapi4 = Region(2171,542,561,45)
rMenuZaapi5 = Region(2171,593,569,52)
rMenuZaapi6 = Region(2170,652,569,48)
rMenuZaapi7 = Region(2171,706,559,50)
rMenuZaapi8 = Region(2172,765,559,49)
rMenuZaapi9 = Region(2169,821,569,49)
rMenuZaapi10 = Region(2172,878,567,51)
rMenuZaapiListe = [rMenuZaapi1,rMenuZaapi2,rMenuZaapi3,rMenuZaapi4,rMenuZaapi5,rMenuZaapi6,rMenuZaapi7,rMenuZaapi8,rMenuZaapi9,rMenuZaapi10]



#import ScanHDV.ScanHDV
from ScanHDV.ScanHDV import *


class HDV:
    #callback c est le type de l hdv c'est égal a litMenuDroiteRess ou litMenuDroiteItem
    def __init__(self,nom,rPosZaapi,rPosVendeur,nbCat,typeHdv):
        self.nom = nom
        self.rPosZaapi = rPosZaapi
        self.rPosVendeur = rPosVendeur
        self.nbCat = nbCat
        self.typeHdv = typeHdv

    #L'état de base est sur le zaapi fenetre de tp ouverte onglet hdv, donc leave nous fait aller dans cet etat
    def leave(self):
        click(self.rPosZaapi)
        click("1610210844153.png")
        click("1610210876724.png")
    def join(self):
        mouseMove(rMenuZaapi1)
        i = 0
        while i < 10:
            if rMenuZaapiListe[i].text().find(self.nom) != -1:
                click(rMenuZaapiListe[i])
                return
            i = i + 1
        wheel(WHEEL_DOWN, 5)
        i = 0
        while i < 10:
            if rMenuZaapiListe[i].text().find(self.nom) != -1:
                click(rMenuZaapiListe[i])
                return
            i = i + 1
            
    def ouvre(self):
        sleep(0.2)
        click(self.rPosVendeur)
        click("1610245635317.png")

    def fermeHdv(self):
        click("1610245672882.png")






