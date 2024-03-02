import math
import random

# 1. feladat
print('1. feladat')
print(f'A háromszög átfogója: c = {round(math.sqrt(int(input("Kérem, adja meg az egyik befogót: a = "))**2 + int(input("Kérem, adja meg a másik befogót: b = "))**2),1)}')

# 2. feladat
print('\n2. feladat')
def nagyit(a,x):
    return a*x

eredeti = random.randint(10,20)

print(f'Az eredti négyzet oldala {eredeti} cm.')
arany = float(input('Kérem, adja meg a nagyítás mértékét (1-nél nagyobb szám): '))

while arany < 1:
    arany = float(input('Kérem, adja meg a nagyítás mértékét (1-nél nagyobb szám): '))

print(f'A felnagyított négyzet oldala {nagyit(eredeti,arany)} cm.')

# 3. feladat
print('\n3. feladat')

class Meghivo:
    def __init__(self, nev, osztaly, darab):
        self.nev = nev
        self.osztaly = osztaly
        self.darab = darab

    def legtobb_meghivo(self):
        print(f'c) A legtöbb meghívót igénylő tanuló:\ntanuló neve: {self.nev}, osztálya: {self.osztaly}, meghívók száma: {self.darab}')

def ossz_meghivok():
    vegz_meghivok = 0
    for diak in adatok:
        vegz_meghivok += int(diak.darab)
    return vegz_meghivok

def legtobb_meghivo():
    legtobb = adatok[0]
    for diak in adatok:
        if int(diak.darab) > int(legtobb.darab):
            legtobb = diak
    return legtobb

fajl = open('meghivok.txt', 'r', encoding='utf-8')
adatok = []
for sor in fajl:
    adatok.append(Meghivo(*sor.strip().split(';')))

print(f'a) Az állomány {len(adatok)} adatsort tartalmaz.')
print(f'b) A végzős diákok összesen {ossz_meghivok()} db meghívót igényeltek.')
legtobb_meghivo().legtobb_meghivo()
