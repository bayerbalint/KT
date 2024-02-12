class IdozitettFelirat:
    def __init__(self, idozites, felirat):
        self.idozites = idozites
        self.felirat = felirat

    def SzavakSzama(self):
        return len(self.felirat.split(' '))
    
    def SrtIdozites(self):
        ujidozites = self.idozites.split('-')
        kesz = ""
        for j in range(len(ujidozites)):
            orak = "0" + str(int(ujidozites[j].strip()[:2]) // 60)
            percek = str(int(ujidozites[j].strip()[:2]) % 60)
            masodpercek = str(ujidozites[j].strip()[3:5])
            if len(percek) == 1:
                percek = "0" + percek
            if len(masodpercek) == 1:
                masodpercek = "0" + masodpercek
            if j == 0:
                kesz += orak + ":" + percek + ":" + masodpercek
            if j == 1:
                kesz += " --> " + orak + ":" + percek + ":" + masodpercek
        return kesz

fajl = open('feliratok.txt', 'r', encoding="utf-8")

adatok = []
for index, adat in enumerate(fajl):
    if index % 2 == 0:
        atmeneti = [adat.strip()]
    else:
        atmeneti.append(adat.strip())
        adatok.append(IdozitettFelirat(*atmeneti))

fajl.close()

# 5. feladat
print(f'5. feladat\nAz állományban {len(adatok)} felirat van.\n')

# 7. feladat
def Leghosszabb():
    legtobb = adatok[0]
    for i in adatok:
        if i.SzavakSzama() > legtobb.SzavakSzama():
            legtobb = i
    return legtobb

print(f'7. feladat\n"{Leghosszabb().felirat}" a legtöbb szóból álló felirat.\n')

# 9. feladat
felirat = open('felirat.srt', 'w', encoding="utf-8")
for ind, par in enumerate(adatok):
    felirat.write(f"{ind+1}\n")
    felirat.write(f"{par.SrtIdozites()}\n")
    felirat.write(f"{par.felirat}\n\n")

print(len(adatok))

felirat.close()