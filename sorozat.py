import random

def veletlen():
    lotto_lista=[]
    for i in range(0,5,1):
        veletlen_szam:int=random.randint(-100, 100)
        lotto_lista.append(veletlen_szam)
    print(f"\t", end="")
    for i in range (0,len(lotto_lista),1):

        if i ==len(lotto_lista)-1:
            print(lotto_lista[i])
        else:
            print(lotto_lista[i], end="; ")
    return lotto_lista

def egyjegyuek_szama(lotto_listam):
    egyjegyu_szama:int=0
    for i in range(0,len(lotto_listam),1):
        if lotto_listam[i] >=0 and lotto_listam[i]<10:
            egyjegyu_szama+=1
    return egyjegyu_szama

def konzol_kiir(egyjegyu_szama):
    print(f"\tAz egyjegyűek száma: {egyjegyu_szama}")

def file_kiir(egyjegyu_szama):
    fajlnev:str="szamok.txt"
    print(f"Az egyjegyűek száma: {egyjegyu_szama}")
    f=open(fajlnev, "w", encoding="utf-8")
    f.write(f"\tAz egyjegyűek száma: {egyjegyu_szama}")
    f.close()