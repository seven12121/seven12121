#Una funcion que retorna 2 valores 

def calcular_pa (lado,ancho):
    area=lado*ancho
    perimetro=2*lado+2*ancho
    return area,perimetro
resultado=calcular_pa(3,4)
print(resultado,type(resultado))

a=resultado[0]
p=resultado[1]
print("area",a,"perimetro",p)

a,p=calcular_pa(7,10)

print(f"Area {a} Perimetro {p}")
