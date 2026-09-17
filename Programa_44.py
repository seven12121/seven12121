from customtkinter import *
def sumar():
    suma= int(entrada_01.get())+ int(entrada_02.get())
    texto_04.configure(text=suma)

ventanita= CTk()
texto_01=CTkLabel(ventanita, text="Dame A:")
texto_01.pack()
entrada_01=CTkEntry(ventanita)
entrada_01.pack()
texto_02=CTkLabel(ventanita, text="Dame B:")
texto_02.pack()
entrada_02=CTkEntry(ventanita)
entrada_02.pack()
boton=CTkButton (ventanita, text="suma", command=sumar)
boton.pack()

texto_03=CTkLabel(ventanita, text="Resultado")
texto_03.pack()
texto_04=CTkLabel(ventanita, text="0", font=("Arial", 15), text_color="red")
texto_04.pack()


ventanita.mainloop()