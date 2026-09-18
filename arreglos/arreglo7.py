#Sumar todos los elementos.  
numeros=int(input("Dime la cantidad de valores que quieres sumar: "))
cantidad=[0]*numeros
suma=0
for i in range(numeros):
    cantidad[i]=int(input("Dime el valor que quieres sumar: "))
    suma+=cantidad[i]
print(f"Tu valor sumado es de {suma}")