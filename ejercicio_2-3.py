from tkinter import *
import tkinter as tk
import random

ventana= Tk()
ventana.title("Generador de números")
ventana.geometry("400x400")


label_nro_1 = tk.Label(ventana, text="Número 1:")
label_nro_1.grid(row=0, column=0, padx=20, pady=10)

label_nro_2 = tk.Label(ventana, text="Número 2:")
label_nro_2.grid(row=1, column=0, padx=20, pady=10)

label_nro_generado = tk.Label(ventana, text="Númerom generado:")
label_nro_generado.grid(row=2, column=0, padx=20, pady=10)


spinbox_nro_1 = tk.Spinbox(ventana, width=20, from_=-99999, to=99999)
spinbox_nro_1.delete(0, tk.END)
spinbox_nro_1.insert(0, "0")
spinbox_nro_1.grid(row=0, column=1, padx=20, pady=10)

spinbox_nro_2 = tk.Spinbox(ventana, width=20, from_= -99999, to=99999)
spinbox_nro_2.delete(0, tk.END)
spinbox_nro_2.insert(0, "0")
spinbox_nro_2.grid(row=1, column= 1)


entry_nro_generado = tk.Entry(ventana, width=20)
entry_nro_generado.grid(row=2, column=1)

def GenerarNumero():

    nro_1 = int(spinbox_nro_1.get())
    nro_2 = int(spinbox_nro_2.get())
    
    if nro_1 > nro_2:
            nro_1, nro_2 = nro_2, nro_1
    
    nro_generado = random.randint(nro_1, nro_2)

    entry_nro_generado.config(state='normal')  
    entry_nro_generado.delete(0, tk.END)    
    entry_nro_generado.insert(0, str(nro_generado)) 
    entry_nro_generado.config(state='readonly')  

bot_generar = tk.Button(ventana, text="Generar número", command=GenerarNumero)
bot_generar.grid(row=3, column=1, padx=20, pady=10)

ventana.mainloop()
