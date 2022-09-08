# Ejercisio No.5: Dado un mumero entero determine si sus dos ultimos digitos son iguales

print("----------------------------------")
print("-----Dos numeros ultimos iguales----")
print("------------------------------------")

# input
n=int(input("Digite el numero entero: "))

# processing

m=n%100
x=m//10
y=m%10

if x==y:
    M=("Si son iguales")
else:
    M=("No son iguales")
    
    

# output
print("----------------------------")
print("-----RESULTADOS-------------")
print("los dos ultimos son: " + str(M))