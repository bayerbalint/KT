import math
# Két public attribútumban (változóban) add vissza a kör kerületét és területét

# Készíts egy örököst a "kor" osztályhoz "gomb" néven!
# A "gomb" osztály adja vissza a gömb legnagyobb kerületét, a gömbközépponton átmenő metszet területét, valamint a gömb felszínét és térfogatát!


class kor:
    def __init__(self,r):
        self.sugar = r
        self.kerulet = 2*self.sugar*math.pi
        self.terulet = self.sugar**2*math.pi

class gomb(kor):
    def __init__(self, r):
        super().__init__(r)
        self.legnagyobb_kerulet = self.kerulet
        self.gk_atmeno = self.terulet
        self.felszin = 4*self.sugar*math.pi
        self.terfogat = (4*self.sugar**3*math.pi) / 3

Gomb = gomb(13)
print(Gomb.terfogat)