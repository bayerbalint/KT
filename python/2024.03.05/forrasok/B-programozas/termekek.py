print('3. feladat')

class Termek:
    def __init__(self, nev, nettoAr, afakulcs):
        self.nev= nev
        self.nettoAr = nettoAr
        self.afakulcs = afakulcs
    def bruttoArKiszamol(self):
        return self.nettoAr*(self.afakulcs/100+1)

tarolo = []

for i in range(3):
    tarolo.append(Termek(input(f'Adja meg a(z) {i+1}. termék nevét:\n'), int(input(f'Adja meg a(z) {i+1}. termék nettó árát:\n')), int(input(f'Adja meg a(z) {i+1}. termék áfakulcsát:\n'))))

for termek in tarolo:
    print(f'Termék neve: {termek.nev}, nettó ár: {termek.nettoAr} Ft, áfakulcs: {termek.afakulcs}%, bruttó ár: {termek.bruttoArKiszamol()} Ft')