import tkinter as tk

def label2D(ablak, lista): # sorok szama, oszlopok szama
    for index, sor in enumerate(lista):
        Cimkek.append([])
        for oszlop in sor:
            Cimkek[index].append(tk.Label(ablak, text=oszlop, font=('Times New Roman', int(window.winfo_screenheight()/3/len(lista)))))

    for i in range(len(Cimkek)):
        for j in range(len(Cimkek[i])):
            Cimkek[i][j].grid(row=i,column=j)

def beolvasas(lista):
    with open('utvonal3.txt', 'r', encoding='UTF-8') as fajl:
        tmp = fajl.readlines()
    for sor in range(len(tmp)-2):
        lista.append(tmp[sor].strip().split(' '))
    fajl.close()
    return [int(tmp[-2].strip().split(' ')[0]),int(tmp[-2].strip().split(' ')[1]),tmp[-1].strip()]

def kereses(sor, oszlop, cel):
    kezdo_kiiras.place_forget() # Eltűntetem a kezdeti label-t
    Cimkek[sor][oszlop]['bg'] = 'orange' # a kezdő háttérszíne
    for lepes in cel:
        if lepes.upper() == 'J':
            oszlop += 1
            if szamok[sor][oszlop] > szamok[sor][oszlop-1]:
                Cimkek[sor][oszlop]['bg'] = '#1a7332'     # nő: #1a7332
            elif szamok[sor][oszlop] < szamok[sor][oszlop-1]:
                Cimkek[sor][oszlop]['bg'] = '#35f067'     # csökken: #35f067  
            else:
                Cimkek[sor][oszlop]['bg'] = '#26ab49'     # marad: #26ab49

        if lepes.upper() == 'L':
            sor += 1
            if szamok[sor][oszlop] > szamok[sor-1][oszlop]:
                Cimkek[sor][oszlop]['bg'] = '#1a7332'     # nő: #1a7332
            elif szamok[sor][oszlop] < szamok[sor-1][oszlop]:
                Cimkek[sor][oszlop]['bg'] = '#35f067'     # csökken: #35f067  
            else:
                Cimkek[sor][oszlop]['bg'] = '#26ab49'     # marad: #26ab49

# főprogram:
window = tk.Tk()

window.title('Útvonal tervező')

Cimkek = [] # Cimkek: soronkent indexelt 'label'-k
szamok = []
adatok = beolvasas(szamok)

kezdo_sor_index = adatok[0]
kezdo_oszlop_index = adatok[1]
celhoz_mozgasok = adatok[2]

label2D(window, szamok)

kezdo_kiiras = tk.Label(window, text='Kattints az útvonaltervezéshez!', font=(int(window.winfo_screenheight()/len(Cimkek))))
kezdo_kiiras.place(relx=0.5, rely=0.5, anchor='center')

window.bind('<Button-1>', lambda a:kereses(kezdo_sor_index, kezdo_oszlop_index, celhoz_mozgasok))

window.mainloop()