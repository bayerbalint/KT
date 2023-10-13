# A rekurzív gondolat egy olyam feladat-megfogalmazás, melyben egy metódust átparaméterezve addig hívunk újra meg újra, amíg a kilépési feltételt el nem érjük.
# A rekurzióban a METHOD() metódus meghívásának helye a METHOD() metódus!
# A rekurzív metódusok ezek alapján saját magukat hívják meg. A hívásnál új paramétereket adnak át. Ha nincs új paraméter, akkor globális paramétereket kell használni(ez a Python-tól-úgyszolván-,nem áll távol...)
# A rekurzió ciklust váltja ki. A legtöbb rekurzióban ezért nem található ciklus! (Létezik kivétel!)
# Előnye, hogy rövid, elegáns kódokat tudunk létrehozni. Hátránya, hogy -sok hívás esetén -, megzabálja a memóriát.
# Amennyiben számokat keresünk rekurzívan, figyelni kell a tárolási mértékre is, mert hamar ki tudunk lépni egy-egy változó maximális méretéből.
# A rekurzió több modellel is leírható. Amenniyben a rekurzív metódus egy függvény, a pince modell a legjobb leírója: elindulunk lefele egy pince lépcsőjén, és minden lépcsőn hagyunk egy kannát.
# Amikor elérjük a kilépési feltételt (pl. a pincét), a legalsó kannában lévő folyadékot beletöltjük az előző lépcsőn lévő kannába. Mire felérünk a pincéből, minden kanna tartalma valamilyen mértékben megváltozott.
# Ebben az esetben viszont, csak a legfelső kanna tartalma a számunkra érdekes.
# Amennyiben a rekurzív metódus egy eljárás, akkor nincs visszafele lépegetés. Ilyenkor a kilépési feltétel bekövetkezésekor érvényben lévő változó-tartalmakat keressük.

# Programozási taktika:
# 1. lépés: Az eredeti problémát az eredetivel megegyező (nagyon hasonló) részproblémákra bontjuk, mindaddig, amíg az alapesetet el nem érjük.
# 2. lépés: A részproblémák megoldásait összekapcsoljuk.
#     a. Minden rekurzív definíciónak van egy, vagy több alapesete, melynek triviális megoldása van.
#           pl.: rekurzív hatványozás
#               n^k - ha k = 0 return 1
#           pl.: rekurzív faktoriálisnál:
#               n! ha n = 0 return 1
#     b. Minden rekurzív definíciónak van egy, vagy több rekurzív esete, mikor a függvény új paraméterekkel meghívja saját magát.


# rekurzió típusai:
# 1. Hívások száma (a kódon belül) alapján:
#    a. egyszeres rekurzió, mely csak egy hívást tartalmaz;
#    b. többszörös, mikor önmagát többféleképpen paraméterezve hívhatja meg.
# 2. A hívott függvény szerint:
#    a. közvetlen rekurzió, mikor a függvény saját magát hívja;
#    b. közvetett rekurzió, mikor f => g, majd g => f módon valósul mega hívás.
# 3. Nevesítés szerint:
#    a. névvel ellátott rekurzió;
#    b. névtelen (lambda) rekurziók

# Rekurzió adattípusok
# Amikor egy program előre nem látható mennyiségű adatot produkál, a programozó rekurzív módon definiálhatja az adatszerkezetet. Ezt kétféle képpen lehet megtenni, induktív, vagy konduktív módon.
# Tipikus induktív adathalmaz pl.: a N(természetes számok halmaza) : Definíciója:
# Egy természetes szám vagy 0, vagy n + 1 alakú, ahol n egy természetes szám.
# Hasonló a láncolt lista:
# Class csomópont:
#   Következő csomópont = null
#   # mit tárolunk ezen a csomóponton:
#   objektum
# A fenti példából kihagytam a sallangokat :)

# Példa egy konduktív adathalmaz definícióra:
# "Egy string-lánc egy objektum, ahol:
#     ELSO_BETU - egy darab (egyelemű) string
#     TOBBI_BETU - egy string lánc"

# Hasonlít az induktívra, de az pontosan meghatározza, hogy miként megy a feltöltése a string-láncnak