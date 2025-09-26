# IMPORTAR LIBRERÍAS 
import tkinter as tk
from tkinter import ttk
from datetime import datetime
# CREAR VENTANA PRINCIPAL 
ventana_principal = tk.Tk()
ventana_principal.title("Registro de Pacientes")   # Título de la ventana
ventana_principal.geometry("800x900")              # Tamaño de la ventana
#CREAR PESTAÑAS (NOTEBOOK) 
pestañas = ttk.Notebook(ventana_principal)         # Contenedor de pestañas
frame_pacientes = ttk.Frame(pestañas)              # Frame para la pestaña Pacientes
pestañas.add(frame_pacientes, text="Pacientes")    # Añadir pestaña
pestañas.pack(expand=True, fill="both")            # Expandir y rellenar
#FUNCIONES
# Función para enmascarar y validar la fecha de nacimiento
def enmascarar_fecha(texto):
   """
   Da formato automático a la fecha mientras el usuario escribe.
   Ejemplo: 01012000 -> 01-01-2000
   Además, calcula la edad automáticamente cuando la fecha está completa.
   """
   limpio = "".join(filter(str.isdigit, texto))   # Filtra solo números
   formato_final = ""
   if len(limpio) > 8:    # Máximo 8 dígitos (DDMMAAAA)
       limpio = limpio[:8]
   # Formatear en DD-MM-AAAA
   if len(limpio) > 4:
       formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
   elif len(limpio) > 2:
       formato_final = f"{limpio[:2]}-{limpio[2:]}"
   else:
       formato_final = limpio
   # Reemplazar texto actual por el formateado
   if FechaX.get() != formato_final:
       FechaX.delete(0, tk.END)
       FechaX.insert(0, formato_final)
   # Si tiene formato completo (DD-MM-AAAA), calcular edad
   if len(FechaX.get()) == 10:
       fecha_actual = datetime.now().date()
       fecha_nacimiento = datetime.strptime(FechaX.get(), "%d-%m-%Y").date()
       edad = fecha_actual.year - fecha_nacimiento.year
       edadVar.set(edad)
   else:
       edadVar.set("")  # Si está incompleta, dejar vacío
   return True
 
# Función para guardar datos en archivo
def guardar_en_archivo():
   """
   Guarda todos los pacientes registrados en un archivo de texto.
   El archivo se llama 'pacientePeso.txt' y usa separador '|'.
   """
   with open("pacientePeso.txt", "w", encoding="utf-8") as archivo:
       for paciente in paciente_data:
           archivo.write(
               f"{paciente['Nombre']}|"
               f"{paciente['Fecha de Nacimiento']}|"
               f"{paciente['Edad']}|"
               f"{paciente['Genero']}|"
               f"{paciente['Grupo Sanguineo']}|"
               f"{paciente['Tipo de Seguro']}|"
               f"{paciente['Centro Medico']}|"
               f"{paciente['Peso']}\n"
           )
 
# Función para cargar pacientes desde el archivo al programa
def cargar_desde_archivo_pacientes():
   """
   Carga la lista de pacientes desde 'pacientePeso.txt'.
   Si el archivo no existe, lo crea vacío.
   """
   try:
       with open("pacientePeso.txt", "r", encoding="utf-8") as archivo:
           paciente_data.clear()   # Limpiar lista antes de cargar
           for linea in archivo:
               datos = linea.strip().split("|")
               if len(datos) == 8:   # Validar que estén todos los campos
                   paciente = {
                       "Nombre": datos[0],
                       "Fecha de Nacimiento": datos[1],
                       "Edad": datos[2],
                       "Genero": datos[3],
                       "Grupo Sanguineo": datos[4],
                       "Tipo de Seguro": datos[5],
                       "Centro Medico": datos[6],
                       "Peso": datos[7]
                   }
                   paciente_data.append(paciente)
       cargar_treeview()   # Actualizar tabla
   except FileNotFoundError:
       open("pacientePeso.txt", "w", encoding="utf-8").close()
 
# Lista de pacientes en memoria
paciente_data = []
# Función para registrar paciente desde el formulario
def registrarPaciente():
   """
   Obtiene los datos del formulario y los agrega a la lista de pacientes.
   Luego actualiza la tabla y guarda en archivo.
   """
   paciente = {
       "Nombre": nombreX.get(),
       "Fecha de Nacimiento": FechaX.get(),
       "Edad": edadVar.get(),
       "Genero": genero.get(),
       "Grupo Sanguineo": entryGrupSan.get(),
       "Tipo de Seguro": tipo_seguro.get(),
       "Centro Medico": centro_medico.get(),
       "Peso": pesoX.get()
   }
   paciente_data.append(paciente)
   cargar_treeview()
   guardar_en_archivo()   # Guardar cambios en el archivo
 
# Función para cargar datos en la tabla Treeview
def cargar_treeview():
   """
   Limpia y vuelve a llenar la tabla con los pacientes actuales.
   """
   # Limpiar tabla
   for paciente in treeview.get_children():
       treeview.delete(paciente)
   # Insertar datos fila por fila
   for i, item in enumerate(paciente_data):
       treeview.insert(
           "", "end", iid=str(i),
           values=(
               item["Nombre"],
               item["Fecha de Nacimiento"],
               item["Edad"],
               item["Genero"],
               item["Grupo Sanguineo"],
               item["Tipo de Seguro"],
               item["Centro Medico"],
               item["Peso"]
           )
       )
# CAMPOS DE FORMULARIO
# Nombre
labelNombre = tk.Label(frame_pacientes, text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreX = tk.Entry(frame_pacientes)
nombreX.grid(row=0, column=1, sticky="w", padx=5, pady=5)
# Fecha de nacimiento con validación
labelFecha = tk.Label(frame_pacientes, text="Fecha de nacimiento (DD-MM-AAAA): ")
labelFecha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
validacion_fecha = ventana_principal.register(enmascarar_fecha)
FechaX = ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
FechaX.grid(row=1, column=1, sticky="w", padx=5, pady=5)
# Edad (solo lectura, se calcula automáticamente)
labelEdad = tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar = tk.StringVar()
edadX = tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
edadX.grid(row=2, column=1, sticky="w", pady=5, padx=5)
# Género (radio buttons)
labelGenero = tk.Label(frame_pacientes, text="Género: ")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero = tk.StringVar()
genero.set("Masculino")   # Valor por defecto
radioMasculino = ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino = ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
# Grupo sanguíneo
labelGrupSan = tk.Label(frame_pacientes, text="Grupo Sanguíneo: ")
labelGrupSan.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupSan = tk.Entry(frame_pacientes)
entryGrupSan.grid(row=5, column=1, sticky="w", pady=5, padx=5)
# Tipo de seguro (combobox)
labelTipSeg = tk.Label(frame_pacientes, text="Tipo de seguro: ")
labelTipSeg.grid(row=6, column=0, pady=5, padx=5, sticky="w")
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipSeg = ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipSeg.grid(row=6, column=1, pady=5, padx=5, sticky="w")
# Centro médico (combobox)
labelCentMed = tk.Label(frame_pacientes, text="Centro de Salud: ")
labelCentMed.grid(row=7, column=0, pady=5, padx=5, sticky="w")
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentMed = ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentMed.grid(row=7, column=1, pady=5, padx=5, sticky="w")
# Peso del paciente
labelPeso = tk.Label(frame_pacientes, text="Peso (kg): ")
labelPeso.grid(row=8, column=0, pady=5, padx=5, sticky="w")
pesoX = tk.Entry(frame_pacientes)
pesoX.grid(row=8, column=1, pady=5, padx=5, sticky="w")
#BOTONES 
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=9, column=0, columnspan=2, pady=5, sticky="w")
btn_registrar = tk.Button(btn_frame, text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
btn_eliminar = tk.Button(btn_frame, text="Eliminar", command="")  # aún sin función
btn_eliminar.grid(row=0, column=1, padx=5)
#TREEVIEW (TABLA)
treeview = ttk.Treeview(
   frame_pacientes,
   columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM", "Peso"),
   show="headings"
)
# Definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")
treeview.heading("Peso", text="Peso (kg)")
# Ajustar anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
treeview.column("Peso", width=70, anchor="center")
treeview.grid(row=11, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
# Scrollbar para la tabla
scroll_y = ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
scroll_y.grid(row=11, column=2, sticky="ns")


cargar_desde_archivo_pacientes()  # Cargar datos al abrir la app
ventana_principal.mainloop()