#Imprimir una l de asteriscos invertida
# de cierta altura
# * * * *
#       *
#       *
#       *
altura=int (input())
for i in range(altura):
    if i==0:
        print ("*"*altura)
    else:
        print(" "*(altura-1)+"*")