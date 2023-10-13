import random
# számok bekérése, vizsgáljuk hogy mindegyik különböző, a határ: 1-90
# húzások számának bekérése, vizsgáljuk, hogy + egész legyen max. 500000000
# húzások elvégzése, minden esetben 5 különböző szém kell!
# húzások összehasonlítása a tippel, a találatok lejegyzése.
class L5:
    def __init__(self, tippTomb, huzasSzam):
        self.TT = tippTomb
        self.HSZ = huzasSzam

    def egyhuzas(self):
        kihuzottak = []
        for i in range(1,6):
            jo_szam = False
            while not jo_szam:
                Uj_szam = random.randint(1,90)
                if Uj_szam not in kihuzottak:
                    kihuzottak.append(Uj_szam)
                    jo_szam = True
        return kihuzottak

    def hanytalalat(self, Kihuzottak):
        talalatSzamlalo = 0
        for EgyTipp in self.TT:
            for EgySzam in Kihuzottak:
                if EgyTipp == EgySzam:
                    talalatSzamlalo += 1
        return talalatSzamlalo

    def Tesztelo(self):
        Eredmeny = {2:0, 3:0, 4:0, 5:0}
        for i in range(self.HSZ):
            AktualisHuzas = self.egyhuzas()
            TalalatSzam = self.hanytalalat(AktualisHuzas)
            if TalalatSzam > 1:
                Eredmeny[TalalatSzam] += 1
        return Eredmeny

#főprogram
print('LOTTO5 tesztelő alkalmazás') 
tipp = []

for i in range(1,6):
    tippek_rendben = False
    while not tippek_rendben:
        egy_tipp = int(input('Add meg a következő tippedet! 1-90 közötti egész számot kérek '))
        if not tipp.__contains__(egy_tipp) and 1 <= egy_tipp <= 90:
            tipp.append(egy_tipp)
            tippek_rendben = True
tipp.sort()
huzasszam_rendben = False
while not huzasszam_rendben:
    huzasszam = int(input('Kérem a húzások számát 1-50000000 közötti egész számot! '))
    if 1 <= huzasszam <= 50000000:
        huzasszam_rendben = True

peldany = L5(tipp,huzasszam)
print(peldany.Tesztelo())