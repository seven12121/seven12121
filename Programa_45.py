#Crear un programa para calcular distancia entre dos puntos 

from customtkinter import *
def calcular():
    try:
        x1 = float(entrada_x1.get())
        y1 = float(entrada_y1.get())
        x2 = float(entrada_x2.get())
        y2 = float(entrada_y2.get())

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

ventanita = CTk()

ventanita.geometry("500x500+300+300")

texto_01 = CTkLabel(ventanita)
texto_01.pack()

entrada_x1 = CTkEntry(ventanita)
entrada_x1.pack()

texto_02 = CTkLabel(ventanita)
texto_02.pack()

entrada_y1 = CTkEntry(ventanita)
entrada_y1.pack()

texto_03 = CTkLabel(ventanita)
texto_03.pack()


entrada_x2 = CTkEntry(ventanita)
entrada_x2.pack()

texto_04 = CTkLabel(ventanita)
texto_04.pack()

entrada_y2 = CTkEntry(ventanita)
entrada_y2.pack()




ventanita.mainloop()

