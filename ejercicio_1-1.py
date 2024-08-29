#Contador creciente de a 1 unidad.

from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Contador creciente")

label = tk.Label(ventana, text="Contador:")
label.grid(row=0, column=0, padx=20)


entry = tk.Entry(ventana, width=20)
entry.grid(row=0, column=1,padx =20)
entry.insert(0, "0")
entry.config(state='disabled')

con = 0

def Incrementar():
    global con
    con += 1
    entry.config(state='normal')
    entry.delete(0,tk.END)
    entry.insert(0, con)
    entry.config(state='disabled')


bot = tk.Button(ventana, text="+", command=Incrementar)
bot.grid(row=0, column=2, padx=5)

ventana.mainloop()