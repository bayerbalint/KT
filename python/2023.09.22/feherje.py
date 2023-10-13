fajl = open('aminosav.txt', 'r', encoding='utf-8')
eredmeny = open('eredmeny.txt', 'w', encoding='utf-8')
bsa = open('bsa.txt', 'r', encoding='utf-8')

atoms = []
for sor in bsa:
    atoms.append(sor.strip())

tarolo = []
for sor in fajl:
    tarolo.append(sor.strip())

atomtomegek = [['',0] for aminosav in range(int(len(tarolo)/7))]
tomegek = {2:12, 3:1, 4:16, 5:14, 6:32}
atomok = {}
for index, a in enumerate(tarolo):
    if index % 7 == 1:
        lista = []
        lista.append(int(tarolo[index+1]))
        lista.append(int(tarolo[index+2]))
        lista.append(int(tarolo[index+3]))
        lista.append(int(tarolo[index+4]))
        lista.append(int(tarolo[index+5]))
        atomok[a] = lista

def tomeg(listaban, listaba):
    i = -1
    for index, adat in enumerate(listaban):
        if index % 7 != 0 and index % 7 != 1:
            listaba[i][1] += int(adat) * tomegek[index % 7]
        if index % 7 == 0:
            i += 1
            listaba[i][0] += adat

    return sorted(atomtomegek, key=lambda x: x[1])

def feladat4():
    osszes = {'C':0,'H':0,'O':0,'N':0,'S':0}
    indexek = {0:'C',1:'H',2:'O',3:'N',4:'S'}
    for adat in atoms:
        for index, i in enumerate(atomok[adat]):
            osszes[indexek[index]] += i
    osszes['H'] += (len(atomok)-1) * 2
    osszes['O'] += len(atomok)-1
    kiiras = ''
    for item in osszes.items():
        kiiras += f'{str(item[0])} {str(item[1])} '
    print(kiiras)

rendezett_aminosavak = tomeg(tarolo,atomtomegek)
print('3.feladat:')
for aminosavs in rendezett_aminosavak:
    print(f'{str(aminosavs[0])} {aminosavs[1]}')

for aminosavak in rendezett_aminosavak:
    eredmeny.write(str(aminosavak[0])+' '+str(aminosavak[1])+'\n') 

feladat4()



fajl.close()
eredmeny.close()
bsa.close()