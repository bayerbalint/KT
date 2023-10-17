# 2. feladat
fajl = open('helsinki.txt', 'r', encoding='ANSI')
tarolo = []
for sor in fajl:
    tarolo.append(sor.strip().split(' '))

# 3. feladat
print(f"3. feladat:\nPontszerző helyezések száma: {len(tarolo)}")

# 4. feladat
ermek = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
for adat in tarolo:
    ermek[adat[0]] += 1
print(f"4. feladat:\nArany: {ermek['1']}\nEzüst: {ermek['2']}\nBronz: {ermek['3']}\nÖsszesen: {str(ermek['1'] + ermek['2'] + ermek['3'])}")

# 5. feladat
pontok = {'1':7,'2':5,'3':4,'4':3,'5':2,'6':1}
osszes = 0
for data in tarolo:
    osszes += pontok[data[0]]
print(f"5. feladat\nOlimpiai pontok száma: {osszes}")

# 6. feladat
sportok = {}
sportok_lista = []
legtobb = 0
key = ''
for j in tarolo:
    if j[2] in sportok.keys():
        if j[2] == 'kajak–kenu':
            sportok['kajakkenu'] += 1
        else:
            sportok[j[2]] += 1
    elif j[2] == 'kajak–kenu':
        sportok['kajakkenu'] += 1
    else:
        sportok[j[2]] = 1

for szam in sportok.items():
    sportok_lista.append(szam[0])
    sportok_lista.append(int(szam[1]))

for index, num in enumerate(sportok_lista):
    if index % 2 == 1:
        if num > legtobb:
            legtobb = num
            key = sportok_lista[index-1]

if sportok_lista.count(legtobb) > 1:
    print('6. feladat:\nEgyenlő volt az érmek száma')
else:
    print(f'6. feladat:\n{key.capitalize()} sportágban szereztek több érmet')

# 7. feladat
helsinki2 = open('helsinki2.txt', 'w', encoding='ANSI') 
for adat in tarolo:
    pont = pontok[adat[0]]
    if adat[2] == 'kajakkenu':
        helsinki2.write(f"{adat[0]} {adat[1]} {pont} kajak–kenu {adat[3]}\n")
    else:
        helsinki2.write(f"{adat[0]} {adat[1]} {pont} {adat[2]} {adat[3]}\n")

# 8. feladat
helyezes = 0
index = 0
for ind, adat in enumerate(tarolo):
    if int(adat[1]) > helyezes:
        helyezes = int(adat[1])
        index = ind
print(f"8. feladat\nHelyezés: {tarolo[index][0]}\nSportág: {tarolo[index][2]}\nVersenyszám: {tarolo[index][3]}\nSportolók száma: {tarolo[index][1]}")