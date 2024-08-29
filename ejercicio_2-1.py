from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")

label_nro_1 = tk.Label(ventana, text="Primer Número")
label_nro_1.grid(row=0, column=0, padx=20, pady=10)

label_nro_2 = tk.Label(ventana, text="Segundo Número")
label_nro_2.grid(row=1, column=0, padx=20, pady= 10)

label_res = tk.Label(ventana, text="Resaultado")
label_res.grid(row=2, column=0, padx=20, pady=10)

entry_nro_1 = tk.Entry(ventana, width=20)
entry_nro_1.grid(row=0, column=1, padx=5)

entry_nro_2 = tk.Entry(ventana, width=20)
entry_nro_2.grid(row=1, column=1, padx=5)

entry_res = tk.Entry(ventana, width=20)
entry_res.grid(row=2, column=1, padx=5)


def Sumar():

    nro_1 = float(entry_nro_1.get())
    nro_2 = float(entry_nro_2.get())
    res = nro_1 + nro_2

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END) 
    entry_res.insert(0, str(res)) 
    entry_res.config(state='disabled')  

def Restar():

    nro_1 = float(entry_nro_1.get())
    nro_2 = float(entry_nro_2.get())
    res = nro_1 - nro_2

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END)
    entry_res.insert(0, str(res))
    entry_res.config(state='disabled')

def Multiplicar():

    nro_1 = float(entry_nro_1.get())
    nro_2 = float(entry_nro_2.get())
    res = nro_1 * nro_2

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END)
    entry_res.insert(0, str(res))
    entry_res.config(state='disabled')

def Dividir():

    nro_1 = float(entry_nro_1.get())
    nro_2 = float(entry_nro_2.get())
    res = nro_1 / nro_2

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END)
    entry_res.insert(0, str(res))
    entry_res.config(state='disabled')

def Resto():

    nro_1 = float(entry_nro_1.get())
    nro_2 = float(entry_nro_2.get())
    res = nro_1 % nro_2

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END)
    entry_res.insert(0, str(res))
    entry_res.config(state='disabled')

def Reinicio():
    
    entry_nro_1.delete(0, tk.END) 
    entry_nro_2.delete(0, tk.END)  

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END)
    entry_res.config(state='disabled')


bot_suma = tk.Button(ventana, text="   +   ", command=Sumar)
bot_suma.grid(row=3, column=0, padx=20, pady= 10)

bot_resta = tk.Button(ventana, text="   -   ", command=Restar)
bot_resta.grid(row=3, column=1, padx=20, pady=10)

bot_multiplicacion= tk.Button(ventana, text="   *   ", command=Multiplicar)
bot_multiplicacion.grid(row=4, column=0, padx=20, pady=10)

bot_dividir = tk.Button(ventana, text="   /   ", command=Dividir)
bot_dividir.grid(row=4, column=1, padx=20, pady=10)

bot_resto = tk.Button(ventana, text="   %   ", command=Resto)
bot_resto.grid(row=5, column=0, padx=20, pady=10)

bot_clear = tk.Button(ventana, text="   CLEAR   ", command=Reinicio)
bot_clear.grid(row=5, column=1, padx=20, pady=10)

ventana.mainloop()