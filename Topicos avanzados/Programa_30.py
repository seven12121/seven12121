#Una funcion que returna valor

def calcular_hipotenusa(a,b):
    hipotenusa= (a*a+b*b)**0.5
    return hipotenusa

resultado=calcular_hipotenusa(7,3)
print(f"La hiputenusa es: {resultado: 2f}")