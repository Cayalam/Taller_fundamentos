# Ejercisio No.3: Dado un numero entero, determinar si es positivo

print("---------------------------------")
print("-----Numero Entero Positivo------")
print("---------------------------------")

# input
n=int(input("Digite el numero entero: "))

# processing

if 1000<n<9999:
  N=("Si es un numero positivo de cuatro digitos")
      
else:
     N=("No es un numero  de cuatro digitos")

# output
print("----------------------")
print("-----RESULTADOS-------")
print("El numero es : " + str(N))


