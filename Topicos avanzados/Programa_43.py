import customtkinter as ctk
def imprimir():
    nombre=entrada.get()
    print(nombre)
ventanita= ctk.CTk()
ventanita.geometry("500x500+200+200")
texto= ctk.CTkLabel(ventanita, text="Dame tu nombre")
texto.pack()
entrada= ctk.CTkEntry(ventanita)
entrada.pack()
boton= ctk.CTkButton(ventanita, text="imprimir", command=imprimir)
boton.pack()

ventanita.mainloop()