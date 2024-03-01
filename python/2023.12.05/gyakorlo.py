class maganhangzok:
    def __init__(self, szoveg):
        self.szoveg = szoveg
        
    def betukSzama(self, betuk):
        szam = 0
        for i in self.szoveg:
            if i.lower() in betuk:
                szam += 1
        return szam
    
    def betuStatisztika(self, betuk):
        stat = {}
        for j in betuk:
            if j in self.szoveg:
                stat[j] = 0
        for k in self.szoveg:
            if k.lower() in betuk:
                stat[k] += 1
        return dict(sorted(stat.items(), key=lambda x: x[1], reverse=True))
                
class massalhangzok(maganhangzok):
    def __init__(self, szoveg):
        super().__init__(szoveg)

maganhangzok_lista = "aáeéuúüűoóöőií"
massalhangzok_lista = "bcdfghjklmnpqrstvwxyz"
m = massalhangzok(input("Kérek egy szöveget! "))
print(m.betukSzama(maganhangzok_lista))
print(m.betuStatisztika(maganhangzok_lista))