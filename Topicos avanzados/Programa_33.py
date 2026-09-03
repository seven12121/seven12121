#Funcion para determinar si los angulos de un triangulo suman 180°

def determinar_180 (a=0,b=0,c=0):
    print(a,b,c)
    if a+b+c==180:
        return True
    else:
        return False
    r1=determinar_180()
    print(r1)

    r2=determinar_180(3)
    print(r2)

    r3=determinar_180(7,90)
    print(r3)

    r4=determinar_180(90,70,2)
    print(r4)

    #r5=determinar_180(,,3)
   # print(r5)
    


