import tkinter as tk
import random

class Main:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry(f'800x800+{int(self.master.winfo_screenwidth() / 2) - 400}+{int(self.master.winfo_screenheight() / 2) - 400}')
        self.master.resizable(False,False)
        self.master.title('Színözön')
        self.master.configure(bg='gray')
        
        self.szinek = ['black','green','blue','pink','yellow','red']
        self.gombok = []
        self.tesztek = []

        self.kezdeti_x = 100
        self.kezdeti_y = 250
        self.szelesseg = 50
        self.magassag = 50
        self.korok = 0
        self.sorok = 4
        self.oszlopok = 4
        
        self.uj_kor()
        
        self.master.mainloop()
        
    def gomb_letrehozas(self, x, y, width, height):
        self.eredmeny = []
        for i in range(self.oszlopok):
            self.gombok.append(tk.Button(self.master,background=self.szinek[0],command=lambda j=i:self.szinvaltas(j)))
            self.gombok[i].place(x=x+i*75,y=y,width=width,height=height)

        # ellenorzo gomb
        self.tesztek.append(tk.Button(self.master,text='OK',command=self.teszt))
        self.tesztek[self.korok].place(x=(i+3)*75,y=y,width=width,height=height)

        # eredmenyek
        for i in range(self.oszlopok):
            if i < self.oszlopok / 2:
                self.eredmeny.append(tk.Button(self.master))
                self.eredmeny[i].place(x=6*x+(0.2*i*x),y=y+5, width=width / 3, height=height/3)
            elif i >= self.oszlopok / 2:
                self.eredmeny.append(tk.Button(self.master))
                self.eredmeny[i].place(x=6*x+((i%2)*0.2*x),y=y+height/2, width=width / 3, height=height/3)
            self.eredmeny[i]['state'] = 'disabled'
            self.eredmeny[i]['bg'] = self.master['bg']
            self.eredmeny[i].configure(borderwidth=0)

    def uj_kor(self):
        self.reset()
        self.nyero = [random.choice(self.szinek) for i in range(self.oszlopok)]
        print(self.nyero) # Itt írom ki a nyerő kombinációt <-------------------------------------------------------
        self.gomb_letrehozas(self.kezdeti_x, self.kezdeti_y, self.szelesseg, self.magassag)


    def reset(self):
        for k in self.master.winfo_children():
            k.destroy()
        self.gombok = []
        self.tesztek = []
        self.korok = 0

    def teszt(self):
        self.tesztek[self.korok]['state'] = 'disabled'
        for l in self.gombok:
            l['state'] = 'disabled'
        for m in self.eredmeny:
            m['state'] = 'disabled'

        self.korok += 1
        proba = [k['bg'] for k in self.gombok]
        jo_roszz_helyen = []
        jo_jo_helyen = []

        for ind, szin in enumerate(proba):
            for k in self.eredmeny:
                if szin == self.nyero[ind]:
                    if k['bg'] != 'white' and k['bg'] != 'black':
                        k['bg'] = 'black'
                        k['borderwidth'] = 1
                        jo_jo_helyen.append(szin)
                        break

        for index, color in enumerate(proba):
            for o in self.eredmeny:
                if color in self.nyero and jo_jo_helyen.count(color) + jo_roszz_helyen.count(color) != self.nyero.count(color) and color != self.nyero[index]:
                    if o['bg'] != 'white' and o['bg'] != 'black':
                        o['bg'] = 'white'
                        o['borderwidth'] = 1
                        jo_roszz_helyen.append(color)
                        break

        if self.korok == self.sorok and self.nyero != proba:
            tk.Label(self.master, text='Vesztettél', font=('Ariel', 30), bg=self.master['bg'], borderwidth=0).place(x=400, y=350, anchor='center')
            tk.Button(self.master,text='Új játék', font=('Ariel', 20), bg=self.master['bg'], borderwidth=0, command=self.uj_kor).place(x=400, y=450, anchor='center')
            return

        if proba == self.nyero:
            tk.Label(self.master, text='Nyertél', font=('Ariel', 30), bg=self.master['bg'], borderwidth=0).place(x=400, y=350, anchor='center')
            tk.Button(self.master,text='Új játék', font=('Ariel', 20) , bg=self.master['bg'], borderwidth=0, command=self.uj_kor).place(x=400, y=450, anchor='center')
            return # Put a text to show they won

        self.gombok.clear()

        self.gomb_letrehozas(self.kezdeti_x, self.kezdeti_y+self.korok*25+(self.korok*self.magassag),self.szelesseg,self.magassag)
            
    def szinvaltas(self,index):
        if self.gombok[index]['bg'] == self.szinek[-1]: self.gombok[index]['bg'] = self.szinek[0]
        else: self.gombok[index]['bg'] = self.szinek[self.szinek.index(self.gombok[index]['bg'])+1]

Main()