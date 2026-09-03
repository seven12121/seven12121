
#Funcion muchos parametros 

def calcular_algo(*parametro):
    print(parametro)
    print(type(parametro))

    calcular_algo()
    calcular_algo(4,3)
    calcular_algo(4,6,"Holas")
