import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from time import strftime

class Film:
    def __init__(self, cim, rendezo, mufaj, terem, kezdet, veg):
        self.cim = cim
        self.rendezo = rendezo
        self.mufaj = mufaj
        self.terem = terem
        self.kezdet = kezdet
        self.veg = veg
        self.ertekek = [self.cim, self.rendezo, self.mufaj, self.terem, self.kezdet, self.veg]
        self.szabad_ulohelyek_indexei = [str(i) for i in range(50)]

class Adatok:
    def __init__(self):
        self.Betutipus = ('Times New Roman', 20)
        self.ablak_m = 540
        self.ablak_sz = 960
        self.filmek = []

    def ablak_atmeretezes(self, ablakok):
        # Kikapcsolom az ablakok átméretezésének lehetőségét
        for ablak in ablakok:
            ablak.resizable(False, False)

    def ablak_torles(self, ablakok, metodus):
        # Beállítom a megadott ablaok listában lévő ablakoknak a metódusát, ami akkor kerül meghívásra, ha bezárják
        for elem in ablakok:
            elem.protocol('WM_DELETE_WINDOW', metodus)

    def ablak_kezdo_ertekek(self, ablak, megjelenes, cim, geometria):
        # megjelenes: boolean valtozo megjelenjen-e az ablak vagy nem
        # geometria: az ablak elhelyezkedése (lista ezekkel az értékekkel)
        ablak.title(cim)
        ablak.geometry(f"{int(geometria[0])}x{int(geometria[1])}+{int(geometria[2])}+{int(geometria[3])}")
        ablak.deiconify() if megjelenes else ablak.withdraw() # a megjelenítés változónak megfelelően jelenítem meg az ablakot

    def ablak_csere(self, lathato, nem_lathato):
        lathato.withdraw() # A jelenleg látható ablakot háttérbe helyezem
        nem_lathato.deiconify() # A jelenleg nem látható ablakot előtérbe hozom

    def tablazat_betoltese(self, ablak, tablazat):
        # style: Az ablak stílusa
        # Megváltoztatom az ablak stílusát, hogy megváltoztathassam a táblázat háttérszínét
        style = ttk.Style(ablak)
        style.theme_use('clam')
        style.configure('Treeview', fieldbackground='#009ffb', background='#009ffb')        

        # Táblázathoz adatok
        oszlopok = ['cim', 'rendezo', 'mufaj', 'terem', 'kezdet', 'veg']
        cimek = ['Cím', 'Rendező', 'Műfaj', 'Terem', 'Vetítés kezdete', 'Vetítés vége']
        szelessegek = [200, 100, 200, 100, 100, 100]

        for ind, i in enumerate(oszlopok):
            tablazat.heading(i, text=cimek[ind])
            tablazat.column(i, width=szelessegek[ind])

    def csere_tablazatra(self, lathato, nem_lathato, tablazat):
        self.betoltes() # betöltöm a "self.filmek"-et az "adatok.txt" fájlból, hogy frissüljenek az adatok
        self.ablak_csere(lathato, nem_lathato) # átváltok a táblázat ablakára
        self.tablazat_frissitese(tablazat) # frissítem a táblázatot az új adatokkal

    def tablazat_frissitese(self, tablazat):
        tablazat.delete(*tablazat.get_children()) # kitörlök minden adatot a táblázatból
        for film in self.filmek: # betöltöm az új adatokat
            tablazat.insert(parent='', index=tk.END, values=film.ertekek)

    def kijeloles_ellenorzes(self, tablazat, kivalasztott, metodus, sok, keves):
        # Lekezelem a nulla vagy több kiválasztott sort
        if len(kivalasztott) > 1:
            messagebox.showerror(title='Hiba', message=sok)
        elif len(kivalasztott) == 0:
            messagebox.showerror(title='Hiba', message=keves)
        else:
            for film in self.filmek:
                if Film(*tablazat.item(kivalasztott)['values']).ertekek == film.ertekek:
                    filmem = film
            metodus(kivalasztott, filmem)

    def gombok_letrehozasa(self, ablak, frame, gombok):
        # Beállítok 2 gomb stílust, hogy tudjam mivel mutatni a foglalt és üres székeket
        style = ttk.Style(ablak)
        style.configure('design1.Toolbutton', width=3, font=self.Betutipus)
        style.configure('design2.Toolbutton', width=3, font=self.Betutipus)
        style.map('design1.Toolbutton', background=[('selected', 'green'),('active', 'white'),('!disabled', 'orange')])
        style.map('design2.Toolbutton', background=[('selected', 'orange'),('active', 'white'),('!disabled', 'black'),('disabled', 'black')], foreground=[('selected', 'black'), ('active', 'black'), ('!disabled', 'white'), ('disabled', 'white')])

        # Elhelyezem az összes gombot (egy keretbe)
        for index, gomb in enumerate(gombok):
            if index % 10 == 5:
                ttk.Label(frame, text=index//10+1, width=10, font=self.Betutipus, anchor='center', background='red', foreground='white').grid(row=index//10, column=5)
                gomb.grid(row=index//10, column=6)
            elif index % 10 < 5:
                gomb.grid(row=index//10, column=index%5) 
            else:
                gomb.grid(row=index//10, column=index%5+6)

    def foglalas(self, film, gombok):
        # végigmegyek az összes gombon és ha ki van választva, akkor átállítom a stílusát  
        self.foglalt = False   
        for gomb in gombok:
            if 'selected' in gomb.state() and gomb['style'] == 'design1.Toolbutton':
                gomb['style'] = 'design2.Toolbutton'
                gomb.state(['!selected'])
                self.foglalt = True
            elif 'selected' in gomb.state() and gomb['style'] == 'design2.Toolbutton':
                gomb['style'] = 'design1.Toolbutton'
                gomb.state(['!selected'])

        # frissítem a film szabad helyeit és elmentem
        film.szabad_ulohelyek_indexei = [str(ind) for ind, i in enumerate(gombok) if i['style'] == 'design1.Toolbutton']
        self.mentes()

    def mentes(self):
        # Kiírom az összes film adatait az 'adatok.txt' fájlba
        fajl = open('adatok.txt', 'w', encoding='utf-8')
        for film in self.filmek:
            fajl.write(f'{film.cim}\t{film.rendezo}\t{film.mufaj}\t{film.terem}\t{film.kezdet}\t{film.veg}\n')
            for i in film.szabad_ulohelyek_indexei:
                fajl.write(str(i)+'\t')
            fajl.write('\n')
        fajl.close()

    def betoltes(self):
        # Megpróbálom megnyitni az 'adatok.txt' fájlt, ha létezik, akkor betöltöm a táblázatot, ha nem, akkor nem csinálok semmit (lehet valami üzenet, hogy nincs elmentve semmi)
        try:
            fajl = open('adatok.txt', 'r', encoding='utf-8')
            self.filmek = []
            for index, j in enumerate(fajl):
                if index % 2 == 0:
                    self.filmek.append(Film(*j.strip().split('\t')))
                else:
                    self.filmek[index//2].szabad_ulohelyek_indexei = j.strip().split('\t')
            fajl.close()
        except FileNotFoundError:
            messagebox.showinfo(title='Infó', message='Nincsenek elmentve filmek!')
            fajl = open('adatok.txt', 'w', encoding='utf-8')
            fajl.close()
    
    def ulohelyek_torlese(self, mentes, ablak, gombok, film=None):
        # Megnézem, hogy mentünk-e, utána kitörlök minden elemet az ablakból
        if mentes:
            self.foglalas(film, gombok)
        for elem in ablak.winfo_children():
            elem.destroy()
        ablak.withdraw()

    def ulohelyek_betoltese(self, film, gombok, disabled=False):
        # Frissítem a gombok stílusát a felületen
        for i, gomb in enumerate(gombok):
            if str(i) not in film.szabad_ulohelyek_indexei:
                gomb['style'] = 'design2.Toolbutton'
                if disabled: gomb['state'] = 'disabled'

    def hatter(self, canvas, img):
        canvas.pack()
        canvas.create_rectangle(0, 0, self.ablak_sz, 75, fill='#009ffb', outline='#009ffb')
        canvas.create_rectangle(0, 465, self.ablak_sz, self.ablak_m, fill='#016afe', outline='#016afe')
        canvas.create_image(5, 5, image=img, anchor="nw")

    def my_time(self, label):
        time_string = strftime('%H:%M:%S') # time format 
        label.config(text=time_string)
        label.after(1000,lambda:self.my_time(label)) # time delay of 1000 milliseconds 

class Fooldal(Adatok):
    def __init__(self):
        super().__init__()
        self.foablak = tk.Tk()
        self.ablak_atmeretezes([self.foablak])
        self.img = tk.PhotoImage(file="mozilogo.png")

        self.betoltes()

    def fooldal_letrehozas(self, admin_ablak, fsz_ablak):
        self.ablak_kezdo_ertekek(self.foablak, True, 'Kezdőlap', [self.ablak_sz, self.ablak_m, 200, 200])
        self.hatter(tk.Canvas(self.foablak, width=self.ablak_sz, height=self.ablak_m, bg='#0183fe', highlightthickness=0), self.img)
        self.l1=tk.Label(self.foablak, font=("times", 30,"bold"), fg="white", bg="black")
        self.l1.place(x=405,y=490)
        self.my_time(self.l1)
        tk.Button(self.foablak, command=lambda: self.ablak_csere(self.foablak, admin_ablak), text="Admin", font=self.Betutipus).place(x=120, y=195, width=300, height=150)
        tk.Button(self.foablak, command=lambda: self.ablak_csere(self.foablak, fsz_ablak), text="Felhasználó", font=self.Betutipus).place(x=540, y=195, width=300, height=150)

class Admin(Adatok):
    def __init__(self, foablak):
        super().__init__()
        self.foablak = foablak
        self.felhasznalonev = 'admin' # BEJELENTKEZÉS
        self.jelszo = 'admin'

        self.img = tk.PhotoImage(file="mozilogo.png")

        self.admin_ablak = tk.Toplevel(self.foablak)
        self.admin_tablazat = tk.Toplevel(self.admin_ablak)
        self.adatok = tk.Toplevel(self.admin_tablazat)
        self.ulohelyek = tk.Toplevel(self.admin_tablazat)

        self.ablak_atmeretezes([self.admin_ablak, self.admin_tablazat, self.adatok, self.ulohelyek])
        self.ablak_torles([self.admin_tablazat], lambda:self.ablak_csere(self.admin_tablazat,self.admin_ablak))
        self.ablak_torles([self.admin_ablak], lambda:self.ablak_csere(self.admin_ablak,self.foablak))
        self.ablak_torles([self.adatok], lambda:self.adatok_torlese())

        # Mindegyik ablakot háttérbe helyezem
        for ablak in [self.admin_ablak, self.admin_tablazat, self.adatok, self.ulohelyek]:
            ablak.withdraw()

        self.admin_letrehozas()
        self.admin_tablazat_letrehozas()

    def ido_perce_alakitas(self, ido):
        return int(ido[:2])*60 + int(ido[3:5])

    def bejelentkezes(self, felhasznalonev, jelszo): # Még majd vissza kell jönni
        if felhasznalonev.get() == self.felhasznalonev and jelszo.get() == self.jelszo:
            self.csere_tablazatra(self.admin_ablak, self.admin_tablazat, self.tablazat)
        felhasznalonev.set("")
        jelszo.set("")

    def admin_letrehozas(self):
        self.ablak_kezdo_ertekek(self.admin_ablak, False, 'Admin', [self.ablak_sz, self.ablak_m, 200, 200])
        self.hatter(tk.Canvas(self.admin_ablak, width=self.ablak_sz, height=self.ablak_m, bg='#0183fe', highlightthickness=0), self.img)

        ido = tk.Label(self.admin_ablak, font=("times", 30,"bold"), fg="white", bg="black")
        ido.place(relx=0.5, rely=0.955, anchor='center')
        self.my_time(ido)

        felhasznalo_str = tk.StringVar() # Létrehozok két változót, amiben eltárolom a felhasználónevet és jelszót
        jelszo_str = tk.StringVar()

        # Létrehozom a bejelentkezési felületet
        ttk.Label(self.admin_ablak, text='Felhasználónév', font=self.Betutipus, background='white').place(relx=0.4, rely=0.4, anchor='center')
        ttk.Entry(self.admin_ablak, textvariable=felhasznalo_str, width=12, font=self.Betutipus).place(relx=0.4, rely=0.5, anchor='center')
        ttk.Label(self.admin_ablak, text='Jelszó', width=12, font=self.Betutipus, background='white', anchor='center').place(relx=0.6, rely=0.4, anchor='center')
        jelszo = ttk.Entry(self.admin_ablak, textvariable=jelszo_str, width=12, font=self.Betutipus)
        jelszo.configure(show="*")
        jelszo.place(relx=0.6, rely=0.5, anchor='center')

        tk.Button(self.admin_ablak, text='Bejelentkezés', font=('Times New Roman', 14), command=lambda:self.bejelentkezes(felhasznalo_str,jelszo_str)).place(relx=0.5, rely=0.6, anchor='center')
        tk.Button(self.admin_ablak, text="Exit", font=self.Betutipus, command=lambda: self.ablak_csere(self.admin_ablak, self.foablak)).place(x=875, y=502, width=150, height=65, anchor='center')

    def adat_bekeres_letrehozasa(self, kivalasztott=None, film=None, hozzaad=False):
        # kivalasztott: Ha szerkesztünk, akkor a kiválasztott sor
        # film : A kiválasztott sor adatai filmként
        # hozzaad: egy boolean változó, hogy hozzáadunk vagy szerkesztünk
        self.ablak_kezdo_ertekek(self.adatok, True, 'Adatok', [self.ablak_sz/3, self.ablak_m/3,200+self.ablak_sz*2/6,200+self.ablak_m*2/6])
        self.adatok['bg'] = '#0183fe'

        # Itt tárolom el az adat bekérési felülethez szükséges adatokat
        ertekek = [tk.StringVar(value=film.cim), tk.StringVar(value=film.rendezo), tk.StringVar(value=film.mufaj), tk.StringVar(value=film.terem), tk.StringVar(value=film.kezdet), tk.StringVar(value=film.veg)]
        feliratok = ['Cím', 'Rendező', 'Műfaj', 'Terem', 'Vetítés kezdete', 'Vetítés vége']

        for ind, i in enumerate(ertekek):
            if ind == 3: # Ha a teremhez érünk, akkor létrehozok egy comboboxot a termek értékeivel
                ttk.Label(self.adatok, text=feliratok[ind], anchor='center').place(relx=0.1, rely=(ind+1)*0.12)
                termek = ttk.Combobox(self.adatok, textvariable=ertekek[ind], state='readonly')
                termek['values'] = ['A','B','C','D']
                if hozzaad == False: termek.current(termek['values'].index(film.terem))
                else: termek.current(0)
                termek.place(relx=0.4, rely=(ind+1)*0.12)
            else:
                ttk.Label(self.adatok, text=feliratok[ind], anchor='center').place(relx=0.1, rely=(ind+1)*0.12)
                ttk.Entry(self.adatok, textvariable=i).place(relx=0.4, rely=(ind+1)*0.12)

        tk.Button(self.adatok, text='Ok', command=lambda:self.adat_ellenorzes(Film(*[j.get() for j in ertekek]), hozzaad, kivalasztott, film)).place(relx=0.8, rely=0.85) # Ok
        tk.Button(self.adatok, text='Exit', command=lambda:self.adatok_torlese()).place(relx=0.9, rely=0.85) # Exit

    def adatok_torlese(self):
        for elem in self.adatok.winfo_children():
                elem.destroy()
        self.adatok.withdraw()

    def admin_tablazat_letrehozas(self):
        self.ablak_kezdo_ertekek(self.admin_tablazat, False, 'Admin/Szerkesztés', [self.ablak_sz, self.ablak_m, 200, 200])

        self.hatter(tk.Canvas(self.admin_tablazat, width=self.ablak_sz, height=self.ablak_m, bg='#0183fe', highlightthickness=0), self.img)

        # Létrehozom a táblázatot
        self.tablazat = ttk.Treeview(self.admin_tablazat, columns=('cim','rendezo','mufaj','terem','kezdet','veg'), show='headings')
        self.tablazat_betoltese(self.admin_tablazat, self.tablazat)
        self.tablazat.place(relx=0.5,rely=0.4, anchor='center')

        # Létrehozom és elhelyezem a gombokat
        gombok = ttk.Frame(self.admin_tablazat)
        gombok.place(relx=0.5, rely=0.65, anchor='center')

        tk.Button(gombok, text='Hozzáadás', bg='white', command=lambda:self.adat_bekeres_letrehozasa(None, Film('','','','','',''), True)).pack(side='left')
        tk.Button(gombok, text='Szerkesztés', bg='white', command=lambda:self.kijeloles_ellenorzes(self.tablazat, self.tablazat.selection(), self.adat_bekeres_letrehozasa, 'Egyszerre csak 1 sort lehet szerkeszteni!', 'Ki kell választani 1 sort a szerkesztéshez!')).pack(side='left')
        tk.Button(gombok, text='Törlés', bg='white', command=self.torles).pack(side='left')
        tk.Button(gombok, text='Ülőhelyek szerkesztése', bg='white', command=lambda:self.kijeloles_ellenorzes(self.tablazat, self.tablazat.selection(), self.ulohelyek_letrehozasa, 'Egyszerre csak 1 sort lehet szerkeszteni!', 'Ki kell választani 1 sort a szerkesztéshez!')).pack(side='left')
        tk.Button(self.admin_tablazat, text="Exit", bg='white', font=self.Betutipus, command=lambda: self.ablak_csere(self.admin_tablazat, self.admin_ablak)).place(x=875, y=502, width=150, height=65, anchor='center')

        # Betöltöm a táblázat kezdeti értékeit és beállítom, hogy a Delete gombbal is lehessen törölni
        self.tablazat.bind('<Delete>', lambda a:self.torles())

    def adat_ellenorzes(self, film=None, hozzaad=bool, kivalasztott=None, initialfilm=None):
        # film : a bekért adatok filmként
        # intialfilm : ha szerkesztünk, akkor a kiválasztott film
        for filmem in self.filmek: # végig megyek az összes filmen, ha valamelyik időpontja egybevág a "film" időpontjával és egy terembe vannak akkor hibát dobok fel és újra kérem az adatokat
            if (self.ido_perce_alakitas(filmem.kezdet) < self.ido_perce_alakitas(film.kezdet) < self.ido_perce_alakitas(filmem.veg) or self.ido_perce_alakitas(filmem.kezdet) < self.ido_perce_alakitas(film.veg) < self.ido_perce_alakitas(filmem.veg)) and filmem.terem == film.terem:
                messagebox.showerror(title='Hiba', message='A filmek időpontjai nem vághatnak egybe!')
                self.adatok_torlese()
                self.adat_bekeres_letrehozasa(kivalasztott, initialfilm, hozzaad)
                return

        # Megnézem, hogy van-e üres érték az adatokban
        if '' in [film.cim,film.rendezo,film.mufaj,film.terem,film.kezdet,film.veg]:
            messagebox.showerror(title='Hiba', message='Minden mezőt ki kell tölteni!')
            self.adatok_torlese()
            self.adat_bekeres_letrehozasa(kivalasztott, initialfilm, hozzaad)

        # Megnézem, hogy jó-e az idő formátum
        elif len(film.kezdet) != 5 or len(film.veg) != 5 or film.kezdet[2] != ':' or film.veg[2] != ':':
            messagebox.showerror(title='Hiba', message='Az időt helyes formátumban kell megadni (óó:pp)!')
            self.adatok_torlese()
            self.adat_bekeres_letrehozasa(kivalasztott, initialfilm, hozzaad)

        # Ha hozzáadunk, akkor hozzáadom a táblázathoz, ha nem akkor szerkesztem a kiválasztott filmet
        elif hozzaad:
            self.tablazat.insert(parent='', index=tk.END, values=[film.cim, film.rendezo, film.mufaj, film.terem, film.kezdet, film.veg])
            self.filmek.append(film)
            self.adatok_torlese()
            self.mentes()
        else: 
            self.tablazat.item(kivalasztott, values=[film.cim, film.rendezo, film.mufaj, film.terem, film.kezdet, film.veg])
            for i in self.filmek:
                if [i.cim,i.rendezo,i.mufaj,i.terem,i.kezdet,i.veg] == [initialfilm.cim, initialfilm.rendezo, initialfilm.mufaj, initialfilm.terem, initialfilm.kezdet, initialfilm.veg]:
                    self.filmek[self.filmek.index(i)] = film
            self.adatok_torlese()
            self.mentes()

    def torles(self):
        # Kitörlöm az összes kijelölt sort a táblázatból és mentek
        kijeloltek = []
        for kijelolt in self.tablazat.selection():
            kijeloltek.append(self.tablazat.item(kijelolt)['values'])
        for film in self.filmek:
            if film.ertekek in kijeloltek:
                self.filmek.remove(film)
        for sor in self.tablazat.selection():
            self.tablazat.delete(sor)
        self.mentes()

    def ulohelyek_letrehozasa(self, sor, film):
        self.ablak_kezdo_ertekek(self.ulohelyek, True, f"Ülőhelyek szerkesztése - {film.cim}", [self.ablak_sz*3/4,self.ablak_m*3/4,200+self.ablak_sz/8,200+self.ablak_m/8])
        self.ulohelyek['bg'] = '#0183fe'

        frame = tk.Frame(self.ulohelyek, bg='#0183fe', borderwidth=8)
        frame.pack(pady=50)

        # Létrehozom az összes gombot
        self.gombok = [ttk.Checkbutton(frame, text=i+1, style='design1.Toolbutton') for i in range(50)]
        self.gombok_letrehozasa(self.ulohelyek, frame, self.gombok)

        # Létrehozom a gombokat és beállítom, hogy az ablak bezárásánál is megkérdezze, hogy mentünk-e kilépés előtt, majd betöltöm a film helyeit
        tk.Button(self.ulohelyek, text='Ok', font=('Times New Roman', 16), width=4, command=lambda:self.foglalas(film, self.gombok)).place(relx=0.4, rely=0.75, anchor='center')
        tk.Button(self.ulohelyek, text='Exit', font=('Times New Roman', 16), width=4, command=lambda:self.ulohelyek_torlese(True, self.ulohelyek, self.gombok, film) if messagebox.askyesno(title='Kilépés', message='Szeretne menteni kilépés előtt?') else self.ulohelyek_torlese(False, self.ulohelyek, self.gombok)).place(relx=0.6, rely=0.75, anchor='center')
        self.ablak_torles([self.ulohelyek], lambda:self.ulohelyek_torlese(True, self.ulohelyek, self.gombok, film) if messagebox.askyesno(title='Kilépés', message='Szeretne menteni kilépés előtt?') else self.ulohelyek_torlese(False, self.ulohelyek, self.gombok))
        self.ulohelyek_betoltese(film, self.gombok)

class Felhasznalo(Adatok):
    def __init__(self, foablak, filmek):
        super().__init__()
        self.filmeim = filmek
        self.foablak = foablak
        self.img = tk.PhotoImage(file="mozilogo.png")
        self.Filmek = []

        self.fsz_ablak = tk.Toplevel(self.foablak)
        self.jegyfoglalas_ablak = tk.Toplevel(self.fsz_ablak)
        self.foglalas_ablak = tk.Toplevel(self.jegyfoglalas_ablak)

        self.ablak_atmeretezes([self.fsz_ablak, self.jegyfoglalas_ablak, self.foglalas_ablak])
        self.ablak_torles([self.fsz_ablak], lambda:self.foablak.destroy())
        self.ablak_torles([self.jegyfoglalas_ablak], lambda:self.ablak_csere(self.jegyfoglalas_ablak, self.fsz_ablak))
        self.foglalas_ablak.withdraw()

        self.felhasznalo()
        self.jegyfoglalas()

    def felhasznalo(self):
        # Ez az ablak csak azért van, ha esetleg lesz valami jövőbeli újítás, akkor lehessen több funkciót is hozzáadni
        self.ablak_kezdo_ertekek(self.fsz_ablak, False, 'Felhasználó', [self.ablak_sz, self.ablak_m, 200, 200])
        self.hatter(tk.Canvas(self.fsz_ablak, width=self.ablak_sz, height=self.ablak_m, bg='#0183fe', highlightthickness=0), self.img)
        tk.Button(self.fsz_ablak, text="Exit", bg='white', font=self.Betutipus, command=lambda: self.ablak_csere(self.fsz_ablak, self.foablak)).place(x=875, y=502, width=150, height=65, anchor='center')
        tk.Button(self.fsz_ablak, text="Jegyvásárlás", font=self.Betutipus, command= self.foglalas_betoltese).place(relx=0.5, rely=0.5, width=300, height=150, anchor="center")

    def foglalas_betoltese(self):
        self.csere_tablazatra(self.fsz_ablak, self.jegyfoglalas_ablak, self.tabla)
        # Frissítem a műfajok listáját
        self.Filmek = ['Összes']
        for film in self.filmek:
            if film.cim not in self.Filmek:
                self.Filmek.append(film.cim)
        self.CB['values'] = self.Filmek
        self.CB.current(0)
    
    def siker(self):
        messagebox.showinfo('Siker', 'Sikeres helyfoglalás!')

    def helyek_foglalasa(self, film, gombok):
        self.foglalas(film, gombok)
        messagebox.showinfo('Folyamat', 'Üzenet küldése a terminálnak...')
        if self.foglalt:
            self.foglalas_ablak.after(1000, self.siker)

    def jegyfoglalas(self):
        self.ablak_kezdo_ertekek(self.jegyfoglalas_ablak, False, "Jegyvásárlás", [self.ablak_sz, self.ablak_m, 200, 200])
        self.hatter(tk.Canvas(self.jegyfoglalas_ablak, width=self.ablak_sz, height=self.ablak_m, bg='#0183fe', highlightthickness=0), self.img)

        self.tabla = ttk.Treeview(self.jegyfoglalas_ablak, height=10 ,columns=('cim','rendezo','mufaj','terem','kezdet','veg'), show='headings')
        self.tablazat_betoltese(self.jegyfoglalas_ablak, self.tabla)

        tk.Label(self.jegyfoglalas_ablak, text="Filmek:", bg="#11235A", fg="white", font=self.Betutipus).place(relx=0.16, rely=0.7, anchor="center")

        self.Cb_ertek = tk.StringVar()
        self.CB = ttk.Combobox(self.jegyfoglalas_ablak, textvariable=self.Cb_ertek, values=self.Filmek, state="readonly")
        self.CB.place(relx=0.16, rely=0.75, anchor="center")
        self.CB.bind("<<ComboboxSelected>>", self.betolt)
        self.tabla.place(relx=0.5,rely=0.4,anchor='center')

        tk.Button(self.jegyfoglalas_ablak, text="Exit", bg='white', font=self.Betutipus, command=lambda: self.ablak_csere(self.jegyfoglalas_ablak, self.fsz_ablak)).place(x=875, y=502, width=150, height=65, anchor='center')
        tk.Button(self.jegyfoglalas_ablak, text="Jegyvásárlás", font=self.Betutipus, command= lambda:self.kijeloles_ellenorzes(self.tabla, self.tabla.selection(), self.ulohelyek_letrehozasa,  'Egyszerre csak 1 vetítést lehet kijelölni', 'A jegyvásárláshoz ki kell választani egy vetítést')).place(relx=0.84, rely=0.7, anchor="center")

    def betolt(self, event):
        self.tabla.delete(*self.tabla.get_children())
        if self.Cb_ertek.get() == "Összes":
            for sor in self.filmek:
                self.tabla.insert(parent="", index=tk.END, values=[sor.cim, sor.rendezo, sor.mufaj, sor.terem, sor.kezdet, sor.veg])
        else:
            for sor in self.filmek:
                if sor.cim == self.Cb_ertek.get():
                    self.tabla.insert(parent="", index=tk.END, values=[sor.cim, sor.rendezo, sor.mufaj, sor.terem, sor.kezdet, sor.veg])

    def ulohelyek_letrehozasa(self, sor, film):
        self.ablak_kezdo_ertekek(self.foglalas_ablak, True, f"Ülőhelyek foglalása - {film.cim}", [self.ablak_sz*3/4,self.ablak_m*3/4,200+self.ablak_sz/8,200+self.ablak_m/8])
        self.foglalas_ablak['bg'] = '#0183fe'

        frame = tk.Frame(self.foglalas_ablak, bg='#0183fe')
        frame.place(relx=0.5, rely=0.4, anchor='center')

        self.buttons = [ttk.Checkbutton(frame, text=i+1, style='design1.Toolbutton') for i in range(50)]
        self.gombok_letrehozasa(self.foglalas_ablak, frame, self.buttons)

        tk.Button(self.foglalas_ablak, text='Ok', font=('Times New Roman', 16), width=4, command=lambda:self.helyek_foglalasa(film, self.buttons)).place(relx=0.4, rely=0.75, anchor='center')
        tk.Button(self.foglalas_ablak, text='Exit', font=('Times New Roman', 16), width=4, command=lambda:self.ulohelyek_torlese(True, self.foglalas_ablak, self.buttons, film) if messagebox.askyesno(title='Kilépés', message='Szeretne menteni kilépés előtt?') else self.ulohelyek_torlese(False, self.foglalas_ablak, self.buttons)).place(relx=0.6, rely=0.75, anchor='center')
        self.ablak_torles([self.foglalas_ablak], lambda:self.ulohelyek_torlese(True, self.foglalas_ablak, self.buttons, film) if messagebox.askyesno(title='Kilépés', message='Szeretne menteni kilépés előtt?') else self.ulohelyek_torlese(False, self.foglalas_ablak, self.buttons))

        self.ulohelyek_betoltese(film, self.buttons, True)

class Main(Adatok):
    def __init__(self):
        super().__init__()
        self.ablakok = []

        self.fooldal = Fooldal()
        self.admin = Admin(self.fooldal.foablak)
        self.felhasznalo = Felhasznalo(self.fooldal.foablak, self.admin.filmek)

        self.fooldal.fooldal_letrehozas(self.admin.admin_ablak, self.felhasznalo.fsz_ablak)
        self.fooldal.foablak.mainloop()

if __name__ == '__main__':
    Main()