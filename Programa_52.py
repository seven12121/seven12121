#Realizar un programa en customtkinter para agregar la informacion de estudiantes 
#consultar la informacion de todos los estudiantes, eliminar un estudiante por su numero de control
#modificar la informacion de un estudiante por su numero de control
#la informacion del estudiante es: nombre, numero de control, semestre, promedio
#utilize varios script para desarrollar el proyecto
#1 para la interfaz
#1 para representar toda la interfaz para almacenamiento de la informacion
#otro para las funciones necesarias para que funcione



import json
import os
import customtkinter as ctk
from tkinter import messagebox


ARCHIVO_DATOS = "estudiantes.json"

def cargar_datos():
    """Carga la lista de estudiantes desde el archivo JSON."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []

def guardar_datos(estudiantes):
    """Guarda la lista de estudiantes en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)


def agregar_estudiante(nombre, num_control, semestre, promedio):
    if not nombre or not num_control or not semestre or not promedio:
        return False, "Todos los campos son obligatorios."
    
    estudiantes = cargar_datos()
    
    # Validar si ya existe el número de control
    for est in estudiantes:
        if est["num_control"] == num_control:
            return False, "El número de control ya está registrado."
    
    try:
        semestre_int = int(semestre)
        promedio_float = float(promedio)
    except ValueError:
        return False, "El semestre debe ser un número entero y el promedio un número válido."

    nuevo_estudiante = {
        "nombre": nombre,
        "num_control": num_control,
        "semestre": semestre_int,
        "promedio": promedio_float
    }
    
    estudiantes.append(nuevo_estudiante)
    guardar_datos(estudiantes)
    return True, "Estudiante agregado exitosamente."

def consultar_estudiantes():
    """Retorna la lista completa de estudiantes."""
    return cargar_datos()

def eliminar_estudiante(num_control):
    estudiantes = cargar_datos()
    nuevos_estudiantes = [est for est in estudiantes if est["num_control"] != num_control]
    
    if len(nuevos_estudiantes) == len(estudiantes):
        return False, "No se encontró un estudiante con ese número de control."
    
    guardar_datos(nuevos_estudiantes)
    return True, "Estudiante eliminado correctamente."

def modificar_estudiante(num_control, nombre, semestre, promedio):
    estudiantes = cargar_datos()
    encontrado = False
    
    try:
        semestre_int = int(semestre)
        promedio_float = float(promedio)
    except ValueError:
        return False, "El semestre y promedio deben ser valores numéricos válidos."

    for est in estudiantes:
        if est["num_control"] == num_control:
            est["nombre"] = nombre
            est["semestre"] = semestre_int
            est["promedio"] = promedio_float
            encontrado = True
            break
            
    if not encontrado:
        return False, "No se encontró el número de control a modificar."
        
    guardar_datos(estudiantes)
    return True, "Información del estudiante actualizada correctamente."


# ==========================================
# 3. MÓDULO DE INTERFAZ GRÁFICA
# ==========================================
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class AppEstudiantes(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión de Estudiantes")
        self.geometry("850x500")
        self.resizable(False, False)

        # Configuración de la cuadrícula principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ----------------- PANEL IZQUIERDO: FORMULARIO -----------------
        self.frame_form = ctk.CTkFrame(self, width=320, corner_radius=0)
        self.frame_form.grid(row=0, column=0, sticky="nsew")

        self.label_titulo = ctk.CTkLabel(self.frame_form, text="Datos del Estudiante", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_titulo.pack(pady=20)

        self.entry_nombre = ctk.CTkEntry(self.frame_form, placeholder_text="Nombre completo")
        self.entry_nombre.pack(pady=10, padx=20, fill="x")

        self.entry_control = ctk.CTkEntry(self.frame_form, placeholder_text="Número de Control")
        self.entry_control.pack(pady=10, padx=20, fill="x")

        self.entry_semestre = ctk.CTkEntry(self.frame_form, placeholder_text="Semestre")
        self.entry_semestre.pack(pady=10, padx=20, fill="x")

        self.entry_promedio = ctk.CTkEntry(self.frame_form, placeholder_text="Promedio")
        self.entry_promedio.pack(pady=10, padx=20, fill="x")

        # Botones de Acción
        self.btn_agregar = ctk.CTkButton(self.frame_form, text="Agregar", command=self.accion_agregar)
        self.btn_agregar.pack(pady=10, padx=20, fill="x")

        self.btn_modificar = ctk.CTkButton(self.frame_form, text="Modificar", fg_color="#d97706", hover_color="#b45309", command=self.accion_modificar)
        self.btn_modificar.pack(pady=10, padx=20, fill="x")

        self.btn_eliminar = ctk.CTkButton(self.frame_form, text="Eliminar", fg_color="#dc2626", hover_color="#b91c1c", command=self.accion_eliminar)
        self.btn_eliminar.pack(pady=10, padx=20, fill="x")

        self.btn_limpiar = ctk.CTkButton(self.frame_form, text="Limpiar Campos", fg_color="gray", command=self.limpiar_campos)
        self.btn_limpiar.pack(pady=10, padx=20, fill="x")

        # ----------------- PANEL DERECHO: VISTA / TABLA -----------------
        self.frame_vista = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_vista.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.frame_vista.grid_rowconfigure(1, weight=1)
        self.frame_vista.grid_columnconfigure(0, weight=1)

        self.label_tabla = ctk.CTkLabel(self.frame_vista, text="Estudiantes Registrados", font=ctk.CTkFont(size=15, weight="bold"))
        self.label_tabla.grid(row=0, column=0, pady=10, sticky="w")

        # Cuadro de texto simulando tabla con fuente monoespaciada
        self.textbox_tabla = ctk.CTkTextbox(self.frame_vista, font=("Courier New", 12))
        self.textbox_tabla.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.textbox_tabla.configure(state="disabled")

        # Cargar datos iniciales en la vista
        self.actualizar_vista()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, 'end')
        self.entry_control.delete(0, 'end')
        self.entry_semestre.delete(0, 'end')
        self.entry_promedio.delete(0, 'end')

    def actualizar_vista(self):
        estudiantes = consultar_estudiantes()
        self.textbox_tabla.configure(state="normal")
        self.textbox_tabla.delete("0.0", "end")

        # Cabecera de la tabla
        header = f"{'No. Control':<15} | {'Nombre':<25} | {'Semestre':<10} | {'Promedio':<8}\n"
        self.textbox_tabla.insert("end", header)
        self.textbox_tabla.insert("end", "-" * 68 + "\n")

        for est in estudiantes:
            linea = f"{est['num_control']:<15} | {est['nombre']:<25} | {str(est['semestre']):<10} | {str(est['promedio']):<8}\n"
            self.textbox_tabla.insert("end", linea)

        self.textbox_tabla.configure(state="disabled")

    def accion_agregar(self):
        exito, mensaje = agregar_estudiante(
            self.entry_nombre.get().strip(),
            self.entry_control.get().strip(),
            self.entry_semestre.get().strip(),
            self.entry_promedio.get().strip()
        )
        messagebox.showinfo("Aviso", mensaje)
        if exito:
            self.limpiar_campos()
            self.actualizar_vista()

    def accion_eliminar(self):
        control = self.entry_control.get().strip()
        if not control:
            messagebox.showwarning("Advertencia", "Ingresa el número de control del estudiante que deseas eliminar.")
            return

        exito, mensaje = eliminar_estudiante(control)
        messagebox.showinfo("Aviso", mensaje)
        if exito:
            self.limpiar_campos()
            self.actualizar_vista()

    def accion_modificar(self):
        exito, mensaje = modificar_estudiante(
            self.entry_control.get().strip(),
            self.entry_nombre.get().strip(),
            self.entry_semestre.get().strip(),
            self.entry_promedio.get().strip()
        )
        messagebox.showinfo("Aviso", mensaje)
        if exito:
            self.limpiar_campos()
            self.actualizar_vista()

if __name__ == "__main__":
    app = AppEstudiantes()
    app.mainloop()