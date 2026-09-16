#CLASES Y OBJETOS EN PYTHON
class Persona:


#_init_ es el constructor de una clase en python
def __init__(self, nombre, estatura, edad):
    self._nombre = nombre
    self._estatura = estatura
    self._edad = edad

@property
def nombre (self):
    return self._nombre

@property
def estatura (self):
    return self._estatura

@property
def edad (self):
    return self._edad

def comer (self):
    print("estoy comiendo")

def respirar(self):
    print("estoy respirando")

    def respirar(self):
        print("estoy respirando")
def dormir (self):
    print("estoy durmiendo")


beto = Persona( "alberto", 1.78, 57)


print(f"mi nombre es: {beto.nombre}")
print(f"mi estatura es: {beto.estatura}")
print(f"mi edad es: {beto.edad}")


print()


alex = Persona( "alex", 1.83, 21)
print(f"el nombre es: {alex.nombre}")
print(f"la estatura es: {alex.estatura}")
print(f"la edad es: {alex.edad}")


beto.dormir()
beto. respirar()
beto.comer ()

print()


beto = Persona ("alberto", 1.78, 57)

print(f"mi nombre es: {beto.nombre}")
print(f"mi estatura es: {beto. estatura}")
print (f"mi edad es: {beto.edad}")
    
print ()
alex = Persona ("alex", 1.83, 21)
print (f"el nombre es: {alex. nombre}")
print(f"la estatura es: {alex. estatura}")
print(f"la edad es: {alex. edad}")


beto.dormir()
beto. respirar()
beto.comer ()

print()

alex.dormir()
alex. respirar()
alex.comer()



