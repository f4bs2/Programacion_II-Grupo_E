import tkinter as tk
from tkinter import ttk

# Función para registrar doctores
def guardar_doctor():
    nombre_doctor = campo_nombre.get()
    area_medica = combo_area.get()
    años_exp = spin_años.get()
    sexo = sexo_var.get()
    centro_salud = campo_centro.get()

    if nombre_doctor and area_medica and centro_salud:
        tabla_doctores.insert("", "end", values=(nombre_doctor, area_medica, años_exp, sexo, centro_salud))

        # Limpiar campos
        campo_nombre.delete(0, tk.END)
        combo_area.set("")
        spin_años.delete(0, tk.END)
        spin_años.insert(0, 0)
        sexo_var.set("Masculino")
        campo_centro.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario Médico")
ventana.geometry("700x400")

# Título
etiqueta_titulo = ttk.Label(ventana, text="Formulario de Registro Médico", font=("Arial", 12, "bold"))
etiqueta_titulo.pack(pady=10)

# Frame del formulario
formulario = ttk.Frame(ventana)
formulario.pack(pady=5)

# Campo Nombre
ttk.Label(formulario, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
campo_nombre = ttk.Entry(formulario, width=25)
campo_nombre.grid(row=0, column=1)

# Campo Especialidad
ttk.Label(formulario, text="Área Médica:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
combo_area = ttk.Combobox(formulario, values=["Cardiología", "Pediatría", "Traumatología", "Neurología"], width=22)
combo_area.grid(row=1, column=1)

# Campo Años de experiencia
ttk.Label(formulario, text="Experiencia (años):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
spin_años = tk.Spinbox(formulario, from_=0, to=50, width=5)
spin_años.grid(row=2, column=1, sticky="w")

# Campo Género
ttk.Label(formulario, text="Sexo:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
sexo_var = tk.StringVar(value="Masculino")
radio_masculino = ttk.Radiobutton(formulario, text="Masculino", variable=sexo_var, value="Masculino")
radio_femenino = ttk.Radiobutton(formulario, text="Femenino", variable=sexo_var, value="Femenino")
radio_masculino.grid(row=3, column=1, sticky="w")
radio_femenino.grid(row=4, column=1, sticky="w")

# Campo Hospital
ttk.Label(formulario, text="Centro Médico:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
campo_centro = ttk.Entry(formulario, width=25)
campo_centro.grid(row=5, column=1)

# Botón Registrar
boton_guardar = tk.Button(formulario, text="Registrar", bg="green", fg="white", command=guardar_doctor)
boton_guardar.grid(row=6, columnspan=2, pady=10)

# Tabla de Doctores
columnas_tabla = ("Nombre", "Área Médica", "Experiencia", "Sexo", "Centro Médico")
tabla_doctores = ttk.Treeview(ventana, columns=columnas_tabla, show="headings", height=6)
for columna in columnas_tabla:
    tabla_doctores.heading(columna, text=columna)
    tabla_doctores.column(columna, width=120)
tabla_doctores.pack(fill="x", padx=10, pady=10)

# Ejecutar aplicación
ventana.mainloop()
