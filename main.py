#import ScanHDV.ScanHDV
#import MoveHDV.MoveHDV
from ScanHDV.ScanHDV import *
from MoveHDV.MoveHDV import *


def ecrireFichier(contenu,nomFichier):

    x = getBundleFolder()
    #print(x)
    #print(contenu)
    with open(x + nomFichier, "a") as myfile:
        myfile.write(contenu)

def scan(hdv):
        hdv.ouvre()
        save = litMenuCat(hdv.nbCat, hdv.typeHdv)
        hdv.fermeHdv()
        return save
        


#Conf HDV 

#def __init__(self,nom,rPosZaapi,rPosVendeur,nbCat,typeHdv):
    #Bijoutiers
hdvBijoutiers = HDV("bijoutiers",Region(1876,816,41,69),Region(2343,594,17,52),2,"item")
    #Cordonniers
hdvCordonniers = HDV("cordonniers",Region(2571,463,47,59),Region(2335,754,21,57),2,"item")
    #Tailleurs
hdvTailleurs = HDV("tailleurs",Region(2167,544,43,41),Region(2344,642,18,45),3,"item")
    #Ressources
hdvRessources = HDV("ressources",Region(2896,389,55,65),Region(2106,709,27,55),23,"ress")
    #Bucherons
hdvBucherons = HDV("cheron",Region(2444,339,45,53),Region(2713,818,6,15),5,"ress")
    #Mineurs
hdvMineurs = HDV("mineurs",Region(1875,336,36,34),Region(2105,695,17,31),5,"ress")
    #Forgerons
hdvForgerons = HDV("forgerons",Region(2634,632,36,64),Region(2014,814,20,42),7,"item")
    #Sculpteurs
hdvSculpteurs = HDV("sculpteurs",Region(3099,386,45,53),Region(2568,556,23,35),3,"item")
    #Documents
hdvDocuments = HDV("documents",Region(2488,414,47,45),Region(1877,681,15,25),5,"ress")
    #Runes
hdvRunes = HDV("runes",Region(2036,649,35,53),Region(2016,903,18,36),1,"ress")
    #Alchimistes
hdvAlchimistes = HDV("alchimistes",Region(2913,519,33,56),Region(3130,646,16,35),10,"ress")

listeHDV = [hdvBijoutiers,hdvCordonniers,hdvTailleurs,hdvRessources,hdvBucherons,hdvMineurs,hdvForgerons,hdvSculpteurs,hdvDocuments,hdvRunes,hdvAlchimistes]

def visit (hdv):
    hdv.join()
    wait(1)
    save = scan(hdv)
    hdv.leave()
    return save
#litMenuDroiteRess(rMenuG2)
#scan(hdvBucherons)
#hdvTailleurs.leave()
#visit(hdvBucherons)
#visit(hdvBijoutiers)

i = 0
grosseSaveHdv = " " 

while i < 11:
    now = datetime.now()
    nowStr = now.strftime("_%m_%d_%Y_%H_%M_%S")
    nomSave = "SAVE_HDV_" + listeHDV[i].nom + nowStr + ".csv"
    save = visit(listeHDV[i])
    ecrireFichier(save,nomSave)
    grosseSaveHdv = grosseSaveHdv + save
    i = i + 1

now = datetime.now()
nowStr = now.strftime("_%m_%d_%Y_%H_%M_%S")
nomGrosseSave = "SAVE_HDV_" + nowStr + ".csv"
ecrireFichier(grosseSaveHdv,nomGrosseSave)
    



