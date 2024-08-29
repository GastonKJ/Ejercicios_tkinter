from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Contador creciente y decreciente")

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


def Restar():
    global con
    con -= 1
    entry.config(state='normal')
    entry.delete(0,tk.END)
    entry.insert(0, con)
    entry.config(state='disabled')

def Reinicio():
    global con
    con = 0
    entry.config(state='normal')
    entry.delete(0,tk.END)
    entry.insert(0, con)
    entry.config(state='disabled')


bot = tk.Button(ventana, text="Count Up", command=Incrementar)
bot.grid(row=0, column=2, padx=5)

bot_resta = tk.Button(ventana, text="Count Down", command=Restar)
bot_resta.grid(row=0, column=3, padx=5)

bot_reinicio = tk.Button(ventana, text="Reset", command=Reinicio)
bot_reinicio.grid(row=0, column=4, padx=5)

ventana.mainloop()