
from customtkinter import *

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def agregar_componentes_A(frame):
    CTkLabel(frame, text="Prueba", text_color="white").grid(row=0, column=0)
    CTkButton(frame, text="Sumar").grid(row=1, column=0)

def agregar_componentes_B(frame):
    CTkLabel(frame, text="Datos:").grid(row=0, column=0)
    CTkEntry(frame).grid(row=1, column=0)

estado = True
def cambiar():
    global estado
    if estado == True:
        agregar_componentes_A(frame)
        estado =False
    else:
        agregar_componentes_B(frame)
        estado = True

ventanita = CTk()


frame = CTkFrame(ventanita, fg_color="blue")
frame.pack()

agregar_componentes_A(frame)

agregar_componentes_B(frame)

boton = CTkButton(ventanita, text= "Cambiar", command=cambiar).pack(pady=10)




ventanita.mainloop()