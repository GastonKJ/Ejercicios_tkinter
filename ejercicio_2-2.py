from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Películas")
ventana.geometry("500x300")

label_nombre = tk.Label(ventana, text="Escribe el nombre de una película")
label_nombre.grid(row=0, column=0, padx= 20, pady=10)
label_peliculas = tk.Label(ventana, text="Películas")
label_peliculas.grid(row=0, column=1, padx=70, pady=10)

entry_nombre = tk.Entry(ventana, width=20)
entry_nombre.grid(row=1, column=0, padx=20, pady=10)

lista_peliculas = tk.Listbox(ventana, width=50, height=10)
lista_peliculas.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

def Añadir():

    pelicula = entry_nombre.get()
    if pelicula: 
        lista_peliculas.insert(tk.END, pelicula)  
        entry_nombre.delete(0, tk.END)  


bot_añadir = tk.Button(ventana, text="Añadir", command=Añadir)
bot_añadir.grid(row=2, column=0, padx=20, pady=10)

ventana.mainloop()