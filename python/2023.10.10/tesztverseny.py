# drive-ra  feltölteni a feladatokat!!

# 1. feladat
print('1. feladat: Az adatok beolvasása\n')
valaszok = open('valaszok.txt', 'r', encoding='utf-8')
osszes_valasz = {}
helyes_valaszok = []
for index, adat in enumerate(valaszok):
    if index == 0:
        helyes_valaszok.append(adat.strip())
    else:
        osszes_valasz[adat.strip().split(' ')[0]] = adat.strip().split(' ')[1]

# 2. feladat
print(f"2. fealdat: A vetélkedőn {len(osszes_valasz)} versenyző indult.\n")

# 3. feladat
azonosito = input('3. feladat: A versenyző azonosítója = ')
print(f'{osszes_valasz[azonosito]}   (a versenyző válasza)\n')

# 4. feladat
print('4. feladat:')
print(f"{helyes_valaszok[0]}   (a helyes megoldás)")
eredmeny = ''
for ind, valasz in enumerate(helyes_valaszok[0]):
    if valasz == osszes_valasz[azonosito][ind]:
        eredmeny += "+"
    else:
        eredmeny += " "
print(f"{eredmeny}   (a versenyző helyes válaszai)\n")

# 5. feladat
sorszam = int(input("5. feladat: A feladat sorszáma = ")) -1
helyesek = 0
for i in osszes_valasz.values():
    if i[sorszam] == helyes_valaszok[0][sorszam]:
        helyesek += 1
print(f"A feladatra {helyesek} fő, a versenyzők {str(round(helyesek / len(osszes_valasz) * 100,2))}%-a adott helyes választ.\n")

# 6. feladat
print('6. feladat: A versenyzők pontszámának meghatározása\n')
pontok = open('pontok.txt', 'w', encoding='utf-8')
pontszamok = {}
for j in osszes_valasz.items():
    pontszam = 0
    for index, k in enumerate(j[1]):
        if k == helyes_valaszok[0][index]:
            if 1 <= index <= 5: pontszam += 3
            elif 5 < index <= 10: pontszam += 4
            elif 10 < index <= 13: pontszam += 5
            else: pontszam += 6
    pontok.write(f"{j[0]} {pontszam}\n")
    pontszamok[j[0]] = pontszam

# 7. feladat
print('7. feladat: A verseny legjobbjai:')
rendezett = dict(reversed(sorted(pontszamok.items(),key=lambda item: item[1])))
helyezettek = 0
elozo = 0
for ind, dobogos in enumerate(rendezett.items()):
    if helyezettek < 3:
        if dobogos[1] == elozo:
            print(f"{helyezettek}. díj ({dobogos[1]} pont): {dobogos[0]}")
            helyezettek -= 1
        else:
            print(f"{helyezettek+1}. díj ({dobogos[1]} pont): {dobogos[0]}")
        elozo = dobogos[1]
        helyezettek += 1
    else:
        break