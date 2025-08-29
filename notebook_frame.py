#importamos librerias
import tkinter as tk
from tkinter import ttk

#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("500x700")
ventana_principal.configure(bg="royalBlue")

#Crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)

#Crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
frame_doctores=ttk.Frame(pestañas)

#Agregar pestañas añl Notebook
pestañas.add(frame_pacientes, text="Pacientes")
pestañas.add(frame_doctores, text="Doctores")

#Mostrar las pestañas en las ventanas
pestañas.pack(expand=True, fill="both")    #fill rellena los espacios

#WIDGETS
#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreX=tk.Entry(frame_pacientes)
nombreX.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#Fecha de nacimiento
labelFecha=tk.Label(frame_pacientes, text="Escribir su fecha de nacimiento (DD/MM/AAAA): ")
labelFecha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
FechaX=tk.Entry(frame_pacientes)
FechaX.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#Edad (READONLY)
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadX=tk.Entry(frame_pacientes, state="readonly")
edadX.grid(row=2, column=1, sticky="w")

#Genero
labelGenero=tk.Label(frame_pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino")    #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3,column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)

#Grupo Sanguineo
labelGrupSan=tk.Label(frame_pacientes, text="Grupo Sanguineo: ")
labelGrupSan.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupSan=tk.Entry(frame_pacientes)
entryGrupSan.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#Tipo de Seguro (combobox)
labelTipSeg=tk.Label(frame_pacientes, text="Tipo de seguro: ")
labelTipSeg.grid(row=6, column=0, pady=5,padx=5, sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")   #valor por defecto
comboTipSeg=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipSeg.grid(row=6, column=1, pady=5, padx=5, sticky="w")

#Centro medico
labelCentMed=tk.Label(frame_pacientes, text="Centro de Salud: ")
labelCentMed.grid(row=7, column=0, pady=5,padx=5, sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")   #valor por defecto
comboCentMed=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentMed.grid(row=7, column=1, pady=5, padx=5, sticky="w")

ventana_principal.mainloop()