import tkinter as tk

def rgb_hex(rgb):
        return "#%02x%02x%02x" % rgb 

class SzamlaloAlkalmazas:
    def __init__(self, ablak):
        self.ablak = ablak
        self.ablak.title("Számláló Alkalmazás")
        self.ablak.geometry('400x200')
        self.r=0
        self.g=0
        self.b=0
        self.ablak.configure(bg='black')

        self.ertek = tk.IntVar() #a kiírt szám változója
        self.ertek.set(0)

        #a cimke, amibe kiírjuk a szám értékét:
        self.cimke = tk.Label(ablak, textvariable=self.ertek, font=("Helvetica", 24))
        self.cimke.pack(pady=20)

        gomb_novel = tk.Button(ablak, text="Növel", command=self.novel, font=("Helvetica", 20))
        gomb_novel.pack(side=tk.LEFT, padx=10)

        gomb_csokkent = tk.Button(ablak, text="Csökkent", command=self.csokkent, font=("Helvetica", 20))
        gomb_csokkent.pack(side=tk.RIGHT, padx=10)

        self.label = tk.Label(ablak)

    def novel(self):
        if self.ertek.get() == 0:
            self.label.place_forget()
        if self.b == 255:
            if self.g == 255:
                if self.r == 255:
                    self.label['text'] = 'Innentől fehér vagyok.'
                    self.label.place(relx=0.5, rely=0.5, anchor='center')
                else: self.r+=1
            else: self.g+=1
        else: self.b+=1
        self.ablak['bg'] = rgb_hex((self.r, self.g, self.b))
        self.ertek.set(self.ertek.get() + 1)

    def csokkent(self):
        if self.ertek.get() <= 765:
            self.label.place_forget()
            if self.b == 0:
                if self.g == 0:
                    if self.r == 0:
                        self.label['text'] = 'Innentől fekete vagyok.'
                        self.label.place(relx=0.5, rely=0.5, anchor='center')
                    else: self.r-=1
                else: self.g-=1
            else: self.b-=1
        self.ablak['bg'] = rgb_hex((self.r, self.g, self.b))
        ertek = self.ertek.get()
        if ertek > 0:
            self.ertek.set(ertek - 1)

if __name__ == "__main__":
    ablak = tk.Tk()
    alkalmazas = SzamlaloAlkalmazas(ablak)
    ablak.mainloop()
