import datetime

class adatok:

    def __init__(self,nev,szd,hely,an):
        self.Nev = nev
        self.Szd = szd
        self.Hely = hely
        self.An = an
        
with open('nyersanyag.txt', 'r', encoding='utf-8') as fajl:
    seged = fajl.read()

Tarolo = []

for sor in seged.split("\n"):
    if sor:
        Egyadat = adatok(*sor.split(";"))
        Tarolo.append(Egyadat)
Tarolo.remove(Tarolo[0])

for adat in Tarolo:
    datum_reszek = adat.Szd.split("-")
    jelenlegi = datetime.date(int(datum_reszek[0]), int(datum_reszek[1]), int(datum_reszek[2]))
    kor = (datetime.date.today().year - jelenlegi.year)
    if datetime.date.today().month < jelenlegi.month and datetime.date.today().day < jelenlegi.day:
        kor = (datetime.date.today().year - jelenlegi.year) - 1
    print(adat.Nev,kor,adat.Szd,adat.Hely)
