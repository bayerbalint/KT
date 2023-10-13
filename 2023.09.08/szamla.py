# listaban: hivas kezdete (ora, perc, mp), hivas vege (ora, perc, mp), hivott szam 
fajl = open('hivasok.txt', 'r', encoding='utf-8')
percek = open('percek.txt', 'w', encoding='utf-8')

tarolo = []

for sor in fajl:
    tarolo.append(sor.strip().split('\n'))


# 7:00 - 18:00 : vezetekes(30Ft/perc), mobil(69.175Ft/perc)
# 0:00 - 7:00 és 18:00 - 24:00 : vezetekes(15Ft/perc), mobil(46.675Ft/perc)
# ha csúcsidőben kezdi akkor is annyit kell fizetni



def telefonszam(tel):
    if tel.startswith('39') or tel.startswith('41') or tel.startswith('71'):
        return True
    return False
        


def hivas(idopontok):
    # idopont: ['6 12 3 6 14 8']
    tarol = (idopontok.split(' '))
    if int(tarol[4]) > int(tarol[1]) and int(tarol[3]) == int(tarol[0]):
        if tarol[5] != '0':
            return int(tarol[4]) - int(tarol[1]) + 1
        else:
            return int(tarol[4]) - int(tarol[1]) 
    elif int(tarol[1]) > int(tarol[4]) and int(tarol[0]) < int(tarol[3]):
        if tarol[5] != '0':
            return (int(tarol[4]) + ((int(tarol[3]) - int(tarol[0])) * 60)) - int(tarol[1]) + 1
        else:
            return (int(tarol[4]) + (int(tarol[3]) - int(tarol[0]) * 60)) - int(tarol[1])
    elif int(tarol[1]) == int(tarol[4]) and int(tarol[0]) < int(tarol[3]):
        if tarol[5] != '0':
            return ((int(tarol[3]) - int(tarol[0])) * 60) + 1
        else:
            return ((int(tarol[3]) - int(tarol[0])) * 60)
    else: return 1


telefonszam_in = input("1. Kérek egy telefonszámot! ")

if telefonszam(telefonszam_in):
    print('Ez egy mobil hívószám.\n')
elif telefonszam(telefonszam_in) == False:
    print('Ez egy vezetékes hívószám.\n')

hivas_idopontok = input("2. Kérek egy hívás kezdeti és hívás végi időpontot! (óó pp mp óó pp mp) ")

print(f'A hívás {hivas(hivas_idopontok)} percig tartott.\n')

ertekek = {'csucsidobeni':0, 'nemcsucsidobeni':0, 'mobil':0, 'vezetekes':0, 'csucsertek':0}

for index, hivasok in enumerate(tarolo):
    if index % 2 == 0:
        percek.write(f'{hivas(hivasok[0])}\t {int(tarolo[index+1][0])}\n')
        if 7 <= int(hivasok[0].split(' ')[0]) < 18:
            ertekek['csucsidobeni'] += 1
            if telefonszam(tarolo[index+1][0]):
                ertekek['csucsertek'] += (hivas(hivasok[0]) * 69.175)
            elif telefonszam(tarolo[index+1][0]) == False:
                ertekek['csucsertek'] += (hivas(hivasok[0]) * 30)
        if int(hivasok[0].split(' ')[0]) >= 0 and 7 > int(hivasok[0].split(' ')[0]) or int(hivasok[0].split(' ')[0]) < 24 and int(hivasok[0].split(' ')[0]) >= 18:
            ertekek['nemcsucsidobeni'] += 1
        if telefonszam(tarolo[index+1][0]):
            ertekek['mobil'] += hivas(hivasok[0])
        if telefonszam(tarolo[index+1][0]) == False:
            ertekek['vezetekes'] += hivas(hivasok[0])
        

print(f'4. {ertekek["csucsidobeni"]} hívás történt csúcsidőben és {ertekek["nemcsucsidobeni"]} hívás történt csúcsidőn kívül.\n')
print(f'5. A felhasználó {ertekek["mobil"]} percet beszélt mobil számmal és {ertekek["vezetekes"]} percet beszélt vezetékessel.\n')
print(f'6. A felhasználónak {ertekek["csucsertek"]}Ft-ot kell fizetnie a csúcsdíjas hívásokért.')

fajl.close()
percek.close()