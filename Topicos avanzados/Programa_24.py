#Imprimir la tabla del 2
#Del 1 al 10 
#(Ej. 1x2=2, 2x2=4, 3x2=6, 4x2=8, 5x2=10, 6x2=12, 7x2=14, 8x2=16, 9x2=18 10x2=20)




contador=1
while contador<=10:
    print(f"2 x {contador} = {2*contador}")
    contador=contador+1





    #Y en for 
    for contador in range(1, 11):
        print(f"2 x {contador} = {2*contador}")