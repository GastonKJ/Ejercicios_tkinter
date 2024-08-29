#Contador decreciente de a 1 unidad, iniviando desde el número 88.

from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Contador decreciente")

label = tk.Label(ventana, text="Contador:")
label.grid(row=0, column=0, padx=20)


entry = tk.Entry(ventana, width=20)
entry.grid(row=0, column=1,padx =20)
entry.insert(0, "88")
entry.config(state='disabled')

con = 88

def Restar():
    global con
    con -= 1
    entry.config(state='normal')
    entry.delete(0,tk.END)
    entry.insert(0, con)
    entry.config(state='disabled')


bot = tk.Button(ventana, text="-", command=Restar)
bot.grid(row=0, column=2, padx=5)

ventana.mainloop()