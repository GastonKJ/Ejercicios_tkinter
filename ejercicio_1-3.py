#Calcular factorial.

from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Factorial")
ventana.resizable(True,True)

n = 1

label = tk.Label(ventana, text="n")
label.grid(row=0, column=0, padx=20)

entry = tk.Entry(ventana, width=20)
entry.grid(row=0, column=1,padx =20)
entry.insert(0, n)
entry.config(state='disable')


label_1 = tk.Label(ventana, text="Factorial (n)")
label_1.grid(row=0, column=2, padx=20)

res_fact_entry = tk.Entry(ventana, width=20)
res_fact_entry.grid(row=0, column=3,padx =20)
res_fact_entry.insert(0,"1")
res_fact_entry.config(state='disabled')


def Factorial(nro):
    
    resultado = 1
    for i in range(2, nro + 1):
        resultado = resultado * i
    res_fact_entry.config(state='normal')
    res_fact_entry.delete(0,tk.END)
    res_fact_entry.insert(0,resultado)
    res_fact_entry.config(state='disabled')

def CalcularFactorial():
    global n
    n = n + 1
    entry.config(state='normal')
    entry.delete(0,tk.END)
    entry.insert(0,n)
    entry.config(state='disabled')
    Factorial(n)

bot = tk.Button(ventana, text="Siguiente", command=CalcularFactorial)
bot.grid(row=0, column=4, padx=5)

ventana.mainloop()