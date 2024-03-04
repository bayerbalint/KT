# 1. feladat
def reszekre_osztas(mondat):
    return mondat[len(mondat)//3:len(mondat)*2//3] + mondat[len(mondat)*2//3:] + mondat[:len(mondat)//3]
    

print(reszekre_osztas(input("Kérek egy mondatot! ")))

# Elmélet
# 1. A "self" szó jelentése maga. A szerepe referencia egy példányosított osztályra.
# 2. Az __iadd__ (in place addition) metódus feladata összeadás (osztály példányán "+=" operátor)

# 2. feladat
elso = {i.strip() for i in open("jarat1.txt", "r", encoding="utf-8")}
masodik = {j.strip() for j in open("jarat2.txt", "r", encoding="utf-8")}
harmadik = {k.strip() for k in open("jarat3.txt", "r", encoding="utf-8")}
print(f"Az első járatról a másodikra itt lehet átszállni: {elso & masodik}")
print(f"Az első járatról a harmadikra itt lehet átszállni: {elso & harmadik}")
print(f"A harmadik járatról a másodikra itt lehet átszállni: {harmadik & masodik}")