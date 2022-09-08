print("------------------------------------------------")
print("-----Numero Entero con su ultimo digito par------")
print("--------------------------------------------------")

# input
n=int(input("Digite el numero entero: "))

# processing

if n>=10:
   K= ("El ultimo digito si es par" + str(n % 2==0))
else:
    K=("EL ultimo digito es inpar" + str(n %10))

print("---------------------------")
print("----Resultados-------------")
print("El ultimo digito es: " + str(K))
