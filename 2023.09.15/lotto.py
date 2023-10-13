fajl = open('lottosz.dat', 'r', encoding='utf-8')
lottoki = open('lotto52.ki', 'w', encoding='utf-8')

lottoSzamok = []
for sor in fajl:
    lottoSzamok.append(sor)

lottoSzamok[len(lottoSzamok)-1] += '\n'

utolso_het_szamok = str(input('Kérem az 52. hét lottó számait! '))

utolso_szamok = [eval(i) for i in utolso_het_szamok.strip().split(' ')]
utolso_szamok.sort()

szam = int(input('Kérek egy egész számot (1-51 között) '))

lottos = []

def feladat5():
    kiiras = ''
    for index, k in enumerate(lottoSzamok):
        if index == szam -1:
            kiiras += k
    print(kiiras.strip())

    szamok = [number for number in range(1,91)]
    for l in lottoSzamok:
        for m in l.split(' '):
            lottos.append(eval(m))

    for n in szamok:
        if not lottos.__contains__(n):
            return 'VAN olyan szám, amit egyszer sem húztak ki.'
    return 'NINCS olyan szám, amit egyszer sem húztak ki.'

print(feladat5())

paratlanok = {'paratlan':0}
for o in lottos:
    if o % 2 == 1: paratlanok['paratlan'] += 1
print(f"{paratlanok['paratlan']} páratlan szám volt a kihúzott számok között.")

vissza = ''
for ind, p in enumerate(utolso_szamok):
    if ind == len(utolso_szamok) -1:
        vissza += str(p)
        vissza += '\n'
    else:
        vissza += str(p)
        vissza += ' '
lottoSzamok.append(vissza)

for szamok in lottoSzamok:
    lottoki.write(szamok)

mennyiszer = {}
for num in range(1,91):
    mennyiszer[num] = 0

for q in utolso_szamok:
    lottos.append(q)

for r in lottos:
    mennyiszer[r] += 1


mennyik = ''
for index, s in enumerate(mennyiszer.values()):
    if index % 15 == 0 and index != 0:
        mennyik += '\n'
        mennyik += str(s)
        mennyik += ' '
    else:
        mennyik += str(s)
        mennyik += ' '
        
print(mennyik)

primek = []
for szam in range(2,91):
    prim = True
    for t in range(2,szam):
        if szam % t == 0:
            prim = False
    if prim: primek.append(szam)

nemHuzottPrimek = ''
for u in primek:
    if not lottos.__contains__(u):
        nemHuzottPrimek += str(u) + ' '

print(nemHuzottPrimek)

fajl.close()
lottoki.close()