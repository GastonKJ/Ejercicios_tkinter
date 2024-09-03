#Calculadora 2, con RadioButtons.

from tkinter import *
import tkinter as tk

ventana= Tk()
ventana.title("Generador de números")
ventana.geometry("500x500")


label_valor_1 = tk.Label(ventana, text="Valor 1")
label_valor_1.grid(row=1, column=0, padx=20, pady=10)
label_valor_2 = tk.Label(ventana, text="Valor 2")
label_valor_2.grid(row=2, column=0, padx=20, pady=10)
label_res = tk.Label(ventana, text="Resultado")
label_res.grid(row=3, column=0, padx=20, pady=10)
label_opciones = tk.Label(ventana, text="Operaciones")
label_opciones.grid(row=0, column=2, padx=20, pady=10)

entry_valor_1 = tk.Entry(ventana, width=20)
entry_valor_1.grid(row=1, column=1, padx=20, pady=10)
entry_valor_2 = tk.Entry(ventana, width=20)
entry_valor_2.grid(row=2, column=1, padx=20, pady=10)
entry_res = tk.Entry(ventana, width=20)
entry_res.grid(row=3, column=1, padx=20, pady=10)



operacion = tk.IntVar()
operacion.set(1)

radioButton_sumar = tk.Radiobutton(ventana, text="Sumar", variable= operacion, value=1)
radioButton_sumar.grid(row=1, column=2, padx=20, pady=10)
radioButton_restar = tk.Radiobutton(ventana, text="Restar", variable= operacion, value=2)
radioButton_restar.grid(row=2, column=2, padx=20, pady=10)
radioButton_multiplicar = tk.Radiobutton(ventana, text="Multiplicar", variable= operacion, value=3)
radioButton_multiplicar.grid(row=3, column=2, padx=20, pady=10)
radioButton_dividir = tk.Radiobutton(ventana, text="Dividir", variable= operacion, value=4)
radioButton_dividir.grid(row=4, column=2, padx=20, pady=10)

def Calcular():

    nro_1 = float(entry_valor_1.get())
    nro_2= float(entry_valor_2.get())

    if operacion.get() == 1:  
        res = nro_1 + nro_2
    elif operacion.get() == 2:  
        res = nro_1 - nro_2
    elif operacion.get() == 3: 
        res = nro_1 * nro_2
    elif operacion.get() == 4:
        res = nro_1 / nro_2

    entry_res.config(state='normal')
    entry_res.delete(0, tk.END)
    entry_res.insert(0, res)
    entry_res.config(state='disabled')

bot_calcular = tk.Button(ventana, text="Calcular", command=Calcular)    
bot_calcular.grid(row=4, column=0, padx=20, pady=10)


ventana.mainloop()