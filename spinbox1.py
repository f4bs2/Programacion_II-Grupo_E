#Spinbox de numeros del 1 al 10 para edad
import tkinter as tk
from tkinter import ttk
ventana.geometry("400x500")
ventana=tk.Tk()

def mostrarEdad():
    tk.messagbox.showinfo("Edad",f"La edad seleccionada es:{spin.get()}")
labelEdad=tk.Label(ventana,text="Edad")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventana,text="Obtener valor",command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)
ventana.mainloop()