#Dado el nombre del dia de la 
# semana determinar que numero de 
# dia es, ej. lunes-1, martes-2...

dia=input("Ingresa el nombre del dia de la semana (ej. Lunes.., etc)")
if dia == "Lunes":
    print(1)
elif dia == "Martes":
    print(2)
elif dia == "Miercoles":
    print(3)
elif dia == "Jueves":
    print(4)
elif dia == "Viernes":
    print(5)
elif dia == "Sabado":
    print(6)
elif dia == "Domingo":
    print(7)
else:
    print("No es valido")


