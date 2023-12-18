import tkinter as tk
from tkinter import ttk 

def mehet_Click():
    also = AlsoHatar.get()
    felso = FelsoHatar.get()
    oszto = Oszto.get()

    # LB1 feltöltése:
    LB1.delete(0, tk.END) # kipucolom LB1-et, hátha van már benne valami
    for szam in range(also, felso + 1):
        LB1.insert(tk.END, szam)
        if szam % oszto == 0:
            LB1.itemconfig(tk.END, {'bg':'red'})
            LB1.itemconfig(tk.END, {'fg':'White'})
            
    # LB2 feltöltése        
    LB2.delete(0, tk.END) # kipucolom LB2-et, hátha van már benne valami
    for szam in range(also, felso + 1):
        if szam % oszto == 0:
            LB2.insert(tk.END, szam)

# Főablak
ablak = tk.Tk()
ablak.title("Listbox és NumericUpDown")
ablak.geometry("400x400")
Betutipus = ('Times New Roman', 15, 'bold')

# NumericUpDown vezérlők
AlsoHatar = tk.IntVar()
FelsoHatar = tk.IntVar()
Oszto = tk.IntVar()
Oszto.set("1")
NUD1 = ttk.Spinbox(ablak, from_=0, to=50, textvariable=AlsoHatar, font=Betutipus, state="readonly")
NUD2 = ttk.Spinbox(ablak, from_=0, to=50, textvariable=FelsoHatar, font=Betutipus, state="readonly")
NUD3 = ttk.Spinbox(ablak, from_=1, to=50, textvariable=Oszto, font=Betutipus, state="readonly")
NUD1.place(x=10, y=10, width=80, height=30)
NUD2.place(x=100, y=10, width=80, height=30)
NUD3.place(x=190, y=10, width=80, height=30)

# Gomb létrehozása
mehet_gomb = tk.Button(ablak, text="Mehet", command=mehet_Click)
mehet_gomb.place(x=290, y=10, width=80, height=30)

LB1 = tk.Listbox(ablak, font=Betutipus)
LB2 = tk.Listbox(ablak, font=Betutipus)
LB1.place(x=10 ,y=50, width=80, height=300)
LB2.place(x=100, y=50, width=80, height=300)

ablak.mainloop()

# plusz egy NumericUpDown és az lesz a bizonyos osztó