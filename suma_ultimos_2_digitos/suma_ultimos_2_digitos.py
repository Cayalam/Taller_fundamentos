# Ejercisio No.6: Dado un numero entero, determiar si la sumas de sus dos ultimos digitos es 1 digito


print("-------------------------------------------")
print("-----La suma de los dos ultimos digitos----")
print("-------------------------------------------")

# input
n=int(input("Escriba el numero entero de preferencia: "))

# processing

k=n%100
x=k//10
y=k%10

if x+y<=9:
    K=("Si es de un digto")
else:
    k=("No es de un digto")
    
    

# output
print("----------------------------")
print("-----RESULTADOS-------------")
print("los dos ultimos son: " + str(K))