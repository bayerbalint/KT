class simple:
    def __init__(self, sorszam, pinkod):
        self.sorszam = sorszam
        self.pinkod = pinkod
        self.ervenyes = True
        self.proba = 1
        self.probak = 3

    def ellenorzes(self, pin):
        if self.proba == self.probak:
            self.ervenyes = False
            print("Túl sok helytelen próba, a kártyát érvénytelenítjük!")
        elif self.pinkod == pin:
            print("Sikeres belépés!")
        else:
            self.proba += 1
            print(f"Nem sikerült belépni {3 - self.probak} próbálkozás maradt!")
        
class improved(simple):
    def __init__(self, sorszam, pinkod, puk_kod, egyenleg):
        super().__init__(sorszam, pinkod)
        self.puk_kod = puk_kod
        self.egyenleg = egyenleg

    def ujraaktivalas(self, puk):
        if self.ervenyes:
            print("A kártya már érvényes!")
        elif self.puk_kod == puk:
            self.ervenyes  = True
            print("Sikeres újraaktiválás!")
        elif self.puk_kod != puk:
            print("Helytelen PUK kód!")

    def Egyenleg_kiiras(self):
        print(f'A kártyán kévő egyneleg összege: {self.egyenleg}Ft.')

    def Egyenleg_feltoltes(self, penz):
        try:
            self.egyenleg += penz
            print('Sikeres egyenleg feltöltés!')
        except Exception:
            print('Nem sikerült az egyenleg feltöltése!')

class kartyakezelo:
    def __init__(self):
        self.kartyak = []
    
    def kartya_letrehozas(self, sorszam, pinkod, puk_kod):
        self.kartyak.append(improved(sorszam, pinkod, puk_kod, 0))

kartyaK = kartyakezelo()