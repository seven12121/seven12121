from customtkinter import *

ventanita = CTk()
ventanita.geometry ("400x400+200+200")
texto_01 = CTkLabel(ventanita, text = "Hola")
texto_01.pack()
texto_02 = CTkLabel(ventanita, text="Hola", font=("Arial", 20), text_color="blue")
texto_02.pack()
texto_03 = CTkLabel(ventanita, text="Bienvenido", font=("Arial", 50, "italic"), text_color="red")
texto_03.pack()
ventanita.mainloop()