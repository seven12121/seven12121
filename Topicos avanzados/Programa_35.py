# CLASES Y OBJETOS EN PYTHON

class Persona:
    # __init__ es el constructor de una clase en Python
    def __init__(self, nombre, estatura, edad):
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad

    def comer(self):
        print("estoy comiendo")

    def respirar(self):
        print("estoy respirando")

    def dormir(self):
        print("estoy durmiendo")


# Instancia 1
beto = Persona("alberto", 1.78, 57)

print(f"mi nombre es: {beto.nombre}")
print(f"mi estatura es: {beto.estatura}")
print(f"mi edad es: {beto.edad}")

print("-" * 20)

# Instancia 2 con sus propios datos
alex = Persona("alex", 1.75, 20)

print(f"el nombre es: {alex.nombre}")
print(f"la estatura es: {alex.estatura}")
print(f"la edad es: {alex.edad}")