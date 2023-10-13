import random

class Keno:
    def __init__(self, Tipp, huzasSzam):
        self.TT = Tipp
        self.HSZ = huzasSzam

    def egyhuzas(self):
        kihuzottak = []
        for i in range(1,MegjatszottSzamokSzama+1):
            jo_szam = False
            while not jo_szam:
                Uj_szam = random.randint(1,80)
                if Uj_szam not in kihuzottak:
                    kihuzottak.append(Uj_szam)
                    jo_szam = True
        return kihuzottak
    
    def hanytalalat(self, kihuzott):
        talalatSzamlalo = 0
        for EgyTipp in self.TT:
            for EgySzam in kihuzott:
                if EgyTipp == EgySzam:
                    talalatSzamlalo += 1
        return talalatSzamlalo
    
    def Tesztelo(self):
        nyerok = {1:{1:0},
                  2:{2:0},
                  3:{2:0,3:0},
                  4:{3:0,4:0},
                  5:{3:0,4:0,5:0},
                  6:{0:0,4:0,5:0,6:0},
                  7:{0:0,4:0,5:0,6:0,7:0},
                  8:{0:0,5:0,6:0,7:0,8:0},
                  9:{0:0,5:0,6:0,7:0,8:0,9:0},
                  10:{0:0,5:0,6:0,7:0,8:0,9:0,10:0}}
        for i in range(self.HSZ):
            AktualisHuzas = self.egyhuzas()
            TalalatSzam = self.hanytalalat(AktualisHuzas)
            try:
                nyerok[MegjatszottSzamokSzama][TalalatSzam] += 1
            except:Exception
        return nyerok[MegjatszottSzamokSzama]

print('Kenó tesztelő alkalmazás') 
MegjatszottSzamokSzama = int(input('Hány számmal szeretne játszani? '))
tipp = []

for i in range(1,MegjatszottSzamokSzama+1):
    tippek_rendben = False
    while not tippek_rendben:
        egy_tipp = int(input('Add meg a következő tippedet! 1-80 közötti egész számot kérek '))
        if not tipp.__contains__(egy_tipp) and 1 <= egy_tipp <= 80:
            tipp.append(egy_tipp)
            tippek_rendben = True

tipp.sort()
huzasszam_rendben = False
while not huzasszam_rendben:
    huzasszam = int(input('Kérem a húzások számát 1-10000000 közötti egész számot! '))
    if 1 <= huzasszam <= 10000000:
        huzasszam_rendben = True

objektum = Keno(tipp,huzasszam)
print(objektum.Tesztelo())
