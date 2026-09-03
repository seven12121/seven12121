#Imprimir una L de astericos 
#De altura n, es introducido por teclado 
#Ej.*
#    *
#    *
#    *
#    * * * *

altura=int(input())
for i in range(altura-1):
    print("*")
    print("*" * altura)
    #Checarlo¿?