import tkinter as tk
from tkinter import ttk # themes tkinter - finomabb vezérlők

def szin_valasztas(event):
    if CB_ertek.get() == "Piros":
        szin = "Red"
    elif CB_ertek.get() == "Zöld":
        szin = "Green"
    else:
        szin = "Blue"
    ablak.configure(bg=szin)

# Főprogram:
# Ablak (főablak) létrehozása
ablak = tk.Tk()
ablak.title("Színválasztó")
ablak.geometry("600x400")

# Combobox létrehozása
alapszinek = ["Piros", "Zöld", "Kék"]
CB_ertek = tk.StringVar()
CB = ttk.Combobox(ablak, textvariable=CB_ertek, values=alapszinek, state="readonly")
CB.place(x=10, y=10, width=100, height=30)

# A BIND egy függvény, amely összeköt egy eseményt egy eseménykezelővel
CB.bind("<<ComboboxSelected>>", szin_valasztas)

# Ablak ciklusának indítása. "Főciklus", ami végtelen.
ablak.mainloop()