#Funcion con parametro por defecto 
#Funcion para calcular el cuadrado de un numero 

def calcular_cuadrada (numero=0):
    return numero**2

x=calcular_cuadrada()
print(x)

y=calcular_cuadrada(7)
print(y)