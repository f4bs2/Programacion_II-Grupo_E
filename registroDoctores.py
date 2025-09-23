# Registro de Doctores con Tkinter
import tkinter as tk 
from tkinter import ttk

# Funciones para manejo de archivo
def guardar_datos():
    # Guarda los datos de doctores en un archivo de texto plano
    with open("r_doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in lista_doctores:
            archivo.write(f"{doctor['nombre']}|{doctor['especialidad']}|{doctor['experiencia']}|{doctor['genero']}|{doctor['hospital']}\n")

def cargar_datos():
    # Carga los datos desde el archivo si existe, y actualiza la tabla
    try:
        with open("registro_doctores.txt", "r", encoding="utf-8") as archivo:
            lista_doctores.clear()
            for linea in archivo:
                campos = linea.strip().split("|")
                if len(campos) == 5:
                    doctor = {
                        "nombre": campos[0],
                        "especialidad": campos[1],
                        "experiencia": campos[2],
                        "genero": campos[3],
                        "hospital": campos[4]
                    }
                    lista_doctores.append(doctor)
        actualizar_tabla()
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        open("registro_doctores.txt", "w", encoding="utf-8").close()

# Funciones principales
lista_doctores = []

def registrar_doctor():
    # Captura los datos del formulario y los agrega a la lista
    doctor = {
        "nombre": entrada_nombre.get(),
        "especialidad": seleccion_especialidad.get(),
        "experiencia": entrada_experiencia.get(),
        "genero": seleccion_genero.get(),
        "hospital": seleccion_hospital.get()
    }
    lista_doctores.append(doctor)
    guardar_datos()
    actualizar_tabla()

def actualizar_tabla():
    # Limpia la tabla y la vuelve a llenar con los datos actuales
    for fila in tabla.get_children():
        tabla.delete(fila)

    for i, doctor in enumerate(lista_doctores):
        tabla.insert("", "end", iid=str(i), values=(
            doctor["nombre"],
            doctor["especialidad"],
            doctor["experiencia"],
            doctor["genero"],
            doctor["hospital"]
        ))

# Interfaz Gráfica
ventana = tk.Tk()
ventana.title("Registro de Doctores")
ventana.geometry("900x800")

# Título principal
tk.Label(ventana, text="Registro de Doctores", font=("Candara", 18, "bold")).grid(row=0, column=1, sticky="w", padx=5, pady=5)

# Campo Nombre
tk.Label(ventana, text="Nombre Completo:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Campo Especialidad
tk.Label(ventana, text="Especialidad:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
seleccion_especialidad = tk.StringVar(value="Pediatría")
combo_especialidad = ttk.Combobox(ventana, values=["Pediatría", "Neurología", "Cardiología", "Traumatología"], textvariable=seleccion_especialidad)
combo_especialidad.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Campo Experiencia
tk.Label(ventana, text="Años de Experiencia:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entrada_experiencia = tk.Spinbox(ventana, from_=1, to=60)
entrada_experiencia.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Campo Género
tk.Label(ventana, text="Género:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
seleccion_genero = tk.StringVar(value="Masculino")
ttk.Radiobutton(ventana, text="Masculino", variable=seleccion_genero, value="Masculino").grid(row=5, column=1, sticky="w", padx=5)
ttk.Radiobutton(ventana, text="Femenino", variable=seleccion_genero, value="Femenino").grid(row=6, column=1, sticky="w", padx=5)

# Campo Hospital
tk.Label(ventana, text="Hospital:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
seleccion_hospital = tk.StringVar(value="Hospital Central")
combo_hospital = ttk.Combobox(ventana, values=["Hospital Central", "Hospital Norte", "Clínica Santa María", "Clínica Vida"], textvariable=seleccion_hospital)
combo_hospital.grid(row=7, column=1, sticky="w", padx=5, pady=5)

# Botón para registrar doctor
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")
btn_registrar = tk.Button(frame_botones, text="Registrar", command=registrar_doctor, bg="Green", fg="white")
btn_registrar.grid(row=8, column=0, padx=5)

# Tabla para mostrar doctores registrados
tabla = ttk.Treeview(ventana, columns=("Nombre", "Especialidad", "Experiencia", "Género", "Hospital"), show="headings")
tabla.heading("Nombre", text="Nombre Completo")
tabla.heading("Especialidad", text="Especialidad")
tabla.heading("Experiencia", text="Años de Experiencia")
tabla.heading("Género", text="Género")
tabla.heading("Hospital", text="Hospital")

tabla.column("Nombre", width=120)
tabla.column("Especialidad", width=120)
tabla.column("Experiencia", width=120, anchor="center")
tabla.column("Género", width=120)
tabla.column("Hospital", width=120)

tabla.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

# Carga inicial de datos si el archivo existe
cargar_datos()
actualizar_tabla()

# Ejecuta la aplicación
ventana.mainloop()