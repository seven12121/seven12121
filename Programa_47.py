#Crear un programa que calule la hipotenusa y resuelva una ecuacion de segundo grado 
#Todo en el mismo codigo

from customtkinter import *


def calcular_hipotenusa():
    try:
        a = float(cateto_a.get())
        b = float(cateto_b.get())
        hipotenusa = (a**2 + b**2) ** 0.5
        resultado_label.configure(text=f"Hipotenusa: {hipotenusa:.2f}")
    except ValueError:
        resultado_label.configure(text="Ingresa números válidos")
    

ventanita_hipotenusa = CTk()
ventanita_hipotenusa.title("Calcular Hipotenusa")
ventanita_hipotenusa.geometry("200x200+200+300")


CTkLabel(ventanita_hipotenusa, text="Cateto A").pack()

cateto_a = CTkEntry(ventanita_hipotenusa)
cateto_a.pack()

CTkLabel(ventanita_hipotenusa)

cateto_b = CTkEntry(ventanita_hipotenusa)
cateto_b.pack()

CTkButton(ventanita_hipotenusa, text="Calcular", command=calcular_hipotenusa).pack(pady=10)

resultado_label = CTkLabel(ventanita_hipotenusa, text="Hipotenusa: ")
resultado_label.pack(pady=10)


ventanita_ecuacion = CTkToplevel(ventanita_hipotenusa)
ventanita_ecuacion.title("Resolver Ecuación de Segundo Grado")
ventanita_ecuacion.geometry("260x120+500+300")

CTkLabel(ventanita_ecuacion, text="Ecuación: ax² + bx + c = 0").pack(pady=20)







ventanita_hipotenusa.mainloop()
ventanita_ecuacion.mainloop()