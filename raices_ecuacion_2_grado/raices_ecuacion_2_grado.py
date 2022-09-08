# Ejercicio No.8: Progama para obtener las raices de una ecuacion de  2 grado

print("---------------------------------------------------")
print("----- Raices con ecuacion de segundo grado---------")
print("---------------------------------------------------")

# input
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

# processing
if((b**2)-4*a*c)<0:
    print("La solucion de la ecuacion es con numeros complejos")
    
else:
    x1=(-b+sqtr(b**2-(4*a*c)))/2*a
    x2=(-b-sqtr(b**2-(4*a*c)))/2*a
    
# output
print("------------------------")
print("----- Respuesta---------")
print("La solucion de la ecuacion es: ")
print(+ str(x1))
print(+ str(x2))
