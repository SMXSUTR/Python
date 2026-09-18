#Encontrar el numero mayor
numeros=int(input("Dime la cantidad de valores que quieres calcular cual es el mayor: "))
cantidad=[0]*numeros
cantidad[0]=int(input("Dime tu 1 numero: "))
mayor=cantidad[0]
for i in range(1,numeros):
    cantidad[i]=int(input(f"Dime tu {i+1} numero: "))
    if cantidad[i]>mayor:
        mayor=cantidad[i]
print(f"De tus {len(cantidad)} de numeros, tu numero mayor es {mayor}")