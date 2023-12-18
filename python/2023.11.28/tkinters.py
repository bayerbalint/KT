import tkinter
from tkinter import messagebox
import random

def gombra_kattintas():
    messagebox.showinfo('Gratulálok!', 'Ügyes vagy!')
    ablak.destroy()
    
def gombra_mutat(event):
    uj_x = random.randint(5, ablak.winfo_width() - 5 - gomb.winfo_width())
    uj_y = random.randint(5, ablak.winfo_height() - 5 - gomb.winfo_height())
    gomb.place(x=uj_x,y=uj_y)

# Főprogram
ablak = tkinter.Tk()
ablak.title("Ugráló gomb :)")
ablak.geometry("600x400")

gomb = tkinter.Button(ablak, text="Kattints", width=8, height=2, command=gombra_kattintas)
gomb.place(x=10, y=10)
gomb.bind("<Enter>",gombra_mutat)

ablak.mainloop()
