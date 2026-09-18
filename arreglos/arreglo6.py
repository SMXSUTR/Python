#Contar números pares en el arreglo.
numeros=int(input("Dime el numero de entidades que evaluaremos: "))
cantidad=[0]*numeros
valor=0
for i in range(numeros):
    cantidad[i]=int(input(f"Estamos en el numero {i+1}, dime el numero: "))
    if cantidad[i]%2==0:
        valor+=1
print(f"De tus {len(cantidad)} números, la cantidad de pares es {valor}")