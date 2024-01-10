import bevezetes

#bevezetes.elsofeladat()

import sorozat
print("II/A,B,C:")
lotto_listam=sorozat.veletlen()

print("II/D,E:")
egyjegyuek=sorozat.egyjegyuek_szama(lotto_listam)
sorozat.konzol_kiir(egyjegyuek)

print("II/F:")
sorozat.file_kiir(egyjegyuek)

import autom
print("III/Flotta:")
listam=autom.fajlbeolvasas()
autok_szama=autom.flotta(listam)
print(f"\tAutók száma: {autok_szama}")
print("III/Legfiatalabb")
index=autom.legfiatalabb(listam)
print(f"\tA legfiatalabb autó: {listam[index].nev} ({listam[index].gyartasi_datum})")
print("III/Átlag kor")
atlag=autom.atlag_kor(listam)
