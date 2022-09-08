# Ejercisio taller No.1: ejercisio de la llamada

print("----------------------------")
print("-----Tiempo de la llamada----")
print("-----------------------------")

# input
m=int(input("Digite la cantidad de minutos: "))

# processing
if m <=3:
    total= m * 300
else:
    a= m-3
    total= 300+(a*50)
    

# output
print("----------------------------")
print("-----RESULTADOS-------------")
print("El total a pagar es: " + str(total))