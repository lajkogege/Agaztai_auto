from osztaly import Osztaly
def fajlbeolvasas():
     fajl=open("auto.txt", "r", encoding="utf-8")
     fajl.readline()
     fajbol_sorok_lista=fajl.readlines()
     fajl.close()

     osztaly_lista = []
     for i in range(0, len(fajbol_sorok_lista), 1):
         aktelem = fajbol_sorok_lista[i]
         sor_lista = aktelem.strip().split("$")
         print(sor_lista[0], sor_lista[1])
         osztalyom = Osztaly("bármi", 2)
         osztaly_lista.append(osztalyom)
     return osztaly_lista

def flotta(listam):
    db:int=0
    for i in range(0,len(listam),1):
        db+=1
    return db

def legfiatalabb(listam):
    min:int=100
    index=0
    for i in range(0,len(listam),1):
        if listam[i].gyartasi_ev>min:
            min=listam[i].gyartasi_ev
            index=i
    return index

def atlag_kor(listam):
    atlag:float=0
    osszeg:int=0
    db:int=0
    for i in range(0,len(listam),1):
        osszeg+=2024- listam[i].gyartasi_ev
        db+=1
    atlag= osszeg/db
    return atlag
