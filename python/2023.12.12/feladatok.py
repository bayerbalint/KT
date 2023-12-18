# 1. feladat
def reszekre_osztas(mondat):
    E = ""
    K = ""
    V = ""
    for index, i in enumerate(mondat):
        if index % (len(mondat) // 3) == 0 and E == "" and K == "":
            E = mondat[:index]
        if index % (len(mondat) // 3) == 0 and E != "" and K == "":
            K = mondat[len(E):index]
        if index % (len(mondat) // 3) == 0 and E != "" and K != "":
            if index != len(mondat):
                V = mondat[len(K) + len(E):index+len(mondat)%3]
            else:
                V = mondat[len(K) + len(E):index]
    return K + V + E
    

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