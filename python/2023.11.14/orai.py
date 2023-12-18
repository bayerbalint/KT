# 1. feladat

class Adatok:

    def __init__(self):
        self.tarolo = []

    def feladat2(self, latin_faj):
        for index, hal in enumerate(adatok.tarolo):
            if hal[4] == latin_faj:
                return self.tarolo[index]

adatok = Adatok()

fajl = open("akvariumi_halak.txt", 'r', encoding="ANSI")
for adat in fajl:
    adatok.tarolo.append(adat.strip().split("\t"))
adatok.tarolo.remove(adatok.tarolo[0])
    
    
# 2. feladat
nevek = {}
for i in adatok.tarolo:
    if i[4] not in nevek.keys():
        nevek[i[4]] = 0

kiiras = ""
for j in nevek.keys():
    if j != adatok.tarolo[-1][4]:
        kiiras += f"{j}; "
    else:
        kiiras += f"{j}."

print(f"Magyar halfajok:\n{kiiras}")
    
latinFaj = input("\nKérek egy magyar halfajt a felsoroltak közül: ")
print(adatok.feladat2(latinFaj)[5])

# 2. feladat / b
print(f"\nlatin név: {adatok.feladat2(latinFaj)[5]}\nrend: {adatok.feladat2(latinFaj)[0]}\ncsalád: {adatok.feladat2(latinFaj)[2]}\nlatin család: {adatok.feladat2(latinFaj)[3]}")

# 3. feladat
rendek = {}
for k in adatok.tarolo:
    if k[0] not in rendek.keys():
        rendek[k[0]] = 0
rendeKiiras = ""
for l in rendek.keys():
    if l != adatok.tarolo[-1][0]: rendeKiiras += f"{l}; "
    else: rendeKiiras += f"{l}."

print(f"\nrendek:\n{rendeKiiras}")

rend = input("\nKérek egy rendet a felsoroltak közül: ")

# 3. feladat / b
kiirashoz = ""
for m in adatok.tarolo:
    if m[0] == rend:
        for n in m:
            if n != m[-1] and n != m[0]:
                kiirashoz += f"{n}, "
            elif n == m[-1]:
                kiirashoz += f"{n}; "
print(f"\n{kiirashoz}")