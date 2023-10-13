class Nev:
    def __init__(self, Lista, ertek=0): # ez egy konstruktor
        self.Lista = Lista
        self.Ertek = ertek

    def Eldontes(self):
        for elem in self.Lista:
            if elem == self.Ertek:
                return True
        return False

    def Kivalasztas(self):
        if self.Eldontes():
            for index, elem in enumerate(self.Lista):
                if elem == self.Ertek:
                    return f"A keresett elem indexe: {index}"
        else: return 'Nincs benne az elem a listában.'
    
    def Linkeres(self):
        for index, elem in enumerate(self.Lista):
            if elem == self.Ertek:
                return f"A keresett elem indexe: {index}"
        return 'Nincs benne az elem a listában.'


# Főprogram
# példányosítjuk az osztályt:
# n = Nev() # ez itt még nem tökéletes, mert LEGALÁBB egy listát át kell adnunk
L = [1,2,3,4]
n = Nev(L, 3) # "n" néven példányosíottam a "Nev" osztályt
print(n.Linkeres()) # az "n" osztálypéldányból meghívom az "Eldontes()" metódust