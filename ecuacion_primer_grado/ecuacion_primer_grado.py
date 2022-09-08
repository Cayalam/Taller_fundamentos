# Ejercicio No.7: Resolver una ecuacion de primer grado

print("--------------------------------------")
print("-----Ecuacion de primer grado---------")
print("--------------------------------------")

# input
b=int(input("Ingrese el valor de b: "))
m=int(input("Ingrese el valor de m: "))

# processing
if(m!=0):
    x=(-1*b)/m
else:
    x=("La solucion no existe")

    # output
print("----------------------------")
print("-----RESULTADOS-------------")
print("Solucion de la ecuacion  de primer grado: " + str(x))