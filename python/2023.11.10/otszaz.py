# 1. feladat
fajl = open('penztar.txt','r',encoding="utf-8")

cikkek = []

for adat in fajl:
    cikkek.append(adat.strip())

fajl.close()

# 2. feladat
print("2. feladat")

fizetesek = 0
for cikk in cikkek:
    if cikk == "F":
        fizetesek += 1

print(f"A fizetések száma: {fizetesek}")

# 3. feladat
elso_cikkek = 0
for i in cikkek:
    if i != "F":
        elso_cikkek += 1
    else:
        break
print(f"\n3. feladat\nAz első vásárló {elso_cikkek} darab árucikket vásárolt.")

# 4. feladat
print("\n4. feladat")
vasarlas_sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
arucikk_nev = input("Adja meg egy árucikk nevét! ")
darabszam = int(input("Adja meg a vásárolt darabszámot! "))

# 5. feladat
sorszam = 1
vasarlaskori_sorszam = 0
elso_sorszam = 0
utolso_sorszam = 0
elso = True
vettek = 0
for j in cikkek:
    if j == "F":
        sorszam += 1
    if j == arucikk_nev and vasarlaskori_sorszam != sorszam :
        vettek += 1
    if j == arucikk_nev:
        utolso_sorszam = sorszam
        vasarlaskori_sorszam = sorszam
    if j == arucikk_nev and elso:
        elso_sorszam = sorszam
        elso = False
    
print(f"\n5. feladat\nAz első vásárlás sorszáma: {elso_sorszam}\nAz utolsó vásárlás sorszáma: {utolso_sorszam}\n{vettek} vásárlás során vettek belőle.")

# 6. feladat
print("\n6. feladat")

def ertek(darabszam):
    fizetendo = 0
    if darabszam == 1:
        fizetendo = 500
    elif darabszam == 2:
        fizetendo = 950
    elif darabszam >= 3:
        fizetendo = 1350 + ((darabszam-3)*400)
    return fizetendo

print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")

# 7. feladat
print("\n7. feladat")

vasaroltak = {}
sorszamok = 1

for k in cikkek:
    if k == "F":
        sorszamok += 1
    if sorszamok == vasarlas_sorszam and k != "F" and k not in vasaroltak.keys():
        vasaroltak[k] = 0
    if sorszamok == vasarlas_sorszam and k in vasaroltak.keys() and k != "F":
        vasaroltak[k] += 1

for cikk in vasaroltak.keys():
    print(f"{vasaroltak[cikk]} {cikk}")

# 8. feladat
osszeg = open('osszeg.txt', 'a', encoding="utf-8")
darabok = 0
index = 0
vasarlasok = []
vetelezett = {}

print(cikkek)

for l in cikkek:
    if  index < len(cikkek) and cikkek[index] == "F":
        osszesen = 0
        for value in vetelezett.values():
            osszesen += ertek(value)
        vasarlasok.append(osszesen)
        darabok = 0
        vetelezett = {}
        index += 1
    while (index < len(cikkek) and cikkek[index] != "F"):
        if cikkek[index] not in vetelezett.keys():
            vetelezett[cikkek[index]] = 1
        else:
            vetelezett[cikkek[index]] += 1
        darabok += 1
        index += 1

for ind, ossz in enumerate(vasarlasok):
    osszeg.write(f"{ind+1}: {ossz}\n")

osszeg.close()