#Spinbox de numeros del 1 al 10 para edad
import tkinter as tk
from tkinter import ttk
ventana=tk.Tk()
ventana.geometry("400x500")

#Edad
def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es:{spin.get()}")
labelEdad=tk.Label(ventana,text="Edad")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventana,text="Obtener valor",command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)

#Genero
def mostrarGenero():
    tk.messagebox.showinfo("Genero", f"El genero seleccionado es:{genero.get()}")
labelGenero=tk.Label(ventana, text="Genero")
labelGenero.grid(row=2, column=0, padx=5, pady=10, sticky="w")
#Spinbox de texto para genero
genero=tk.Spinbox(ventana, values=("Masculino", "Femenino", "Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)
botonGenero=tk.Button(ventana, text="Obtener genero", command=mostrarGenero)
botonGenero.grid(row=3, column=0, padx=10, pady=10)

ventana.mainloop()