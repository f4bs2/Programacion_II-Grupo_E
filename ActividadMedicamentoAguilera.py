import tkinter as tk
from tkinter import ttk, messagebox
import os

# Archivo de almacenamiento
ARCHIVO = "medicamento.txt"
SEPARADOR = "|"
medicamento_data = []

# Enmascarar fecha
def formFecha(evento):
    x = entry_fecha_var.get()
    digitos = ''.join(y for y in x if y.isdigit())[:8]
    if len(digitos) > 4:
        formatted = f"{digitos[:2]}-{digitos[2:4]}-{digitos[4:]}"
    elif len(digitos) > 2:
        formatted = f"{digitos[:2]}-{digitos[2:]}"
    else:
        formatted = digitos
    if formatted != x:
        entry_fecha_var.set(formatted)
    entry_fecha.icursor(tk.END)

# Guardar en archivo
def guardar_en_archivo():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for medicamento in medicamento_data:
            archivo.write(
                f"{medicamento['Nombre']}|"
                f"{medicamento['Presentacion']}|"
                f"{medicamento['Dosis']}|"
                f"{medicamento['Fecha']}\n"
            )

# Cargar desde archivo
def cargar_desde_archivo():
    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w", encoding="utf-8").close()
    medicamento_data.clear()
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(SEPARADOR)
            if len(datos) == 4:
                medicamento = {
                    "Nombre": datos[0],
                    "Presentacion": datos[1],
                    "Dosis": datos[2],
                    "Fecha": datos[3]
                }
                medicamento_data.append(medicamento)
    cargar_treeview()

# Registrar medicamento
def registrar_medicamento():
    medicamento = {
        "Nombre": entry_nombre.get().strip(),
        "Presentacion": combo_presentacion.get().strip(),
        "Dosis": entry_dosis.get().strip(),
        "Fecha": entry_fecha_var.get().strip()
    }
    if not all(medicamento.values()):
        messagebox.showwarning("Campos vacíos", "Debe completar todos los campos.")
        return
    medicamento_data.append(medicamento)
    guardar_en_archivo()
    cargar_treeview()
    entry_nombre.delete(0, tk.END)
    combo_presentacion.set("")
    entry_dosis.delete(0, tk.END)
    entry_fecha_var.set("")

# Eliminar medicamento
def eliminar_medicamento():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item = seleccionado[0]
        nombre = treeview.item(id_item, 'values')[0]
        if messagebox.askyesno("Eliminar Medicamento", f"¿Está seguro de eliminar el medicamento '{nombre}'?"):
            del medicamento_data[indice]
            guardar_en_archivo()
            cargar_treeview()
            messagebox.showinfo("Medicamento eliminado", "El medicamento fue eliminado exitosamente.")
    else:
        messagebox.showwarning("Eliminar Medicamento", "No se ha seleccionado ningún medicamento.")

# Cargar datos en Treeview
def cargar_treeview():
    for item in treeview.get_children():
        treeview.delete(item)
    for i, medicamento in enumerate(medicamento_data):
        treeview.insert("", "end", iid=str(i), values=(
            medicamento["Nombre"],
            medicamento["Presentacion"],
            medicamento["Dosis"],
            medicamento["Fecha"]
        ))

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("1000x700")
ventana.minsize(700, 450)

form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)

# Nombre
ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)

# Presentación
ttk.Label(form_frame, text="Presentación:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
combo_presentacion.grid(row=1, column=1, sticky="ew", padx=6, pady=6)

# Dosis
ttk.Label(form_frame, text="Dosis:").grid(row=2, column=0, sticky="w", padx=6, pady=6)
entry_dosis = ttk.Entry(form_frame)
entry_dosis.grid(row=2, column=1, sticky="w", padx=6, pady=6)

# Fecha
ttk.Label(form_frame, text="Fecha Vencimiento (dd-mm-yyyy):").grid(row=3, column=0, sticky="w", padx=6, pady=6)
entry_fecha_var = tk.StringVar()
entry_fecha = ttk.Entry(form_frame, textvariable=entry_fecha_var)
entry_fecha.grid(row=3, column=1, sticky="w", padx=6, pady=6)
entry_fecha.bind("<KeyRelease>", formFecha)

# Botones
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1), weight=1)

tk.Button(btn_frame, text="Registrar", bg="green", fg="white", command=registrar_medicamento).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
tk.Button(btn_frame, text="Eliminar", bg="red", fg="white", command=eliminar_medicamento).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Tabla
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

treeview = ttk.Treeview(list_frame,
                        columns=("nombre", "presentacion", "dosis", "fecha"),
                        show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fecha", text="Fecha Vencimiento")
treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fecha", width=120, anchor="center")

scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)

# Cargar datos al iniciar
cargar_desde_archivo()

# Ejecutar
ventana.mainloop()
