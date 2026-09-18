#Encontrar el numero menor
numeros=int(input("Dime la cantidad de numeros que vas a verificar y te dire tu menor numero: "))
cantidad=[0]*numeros
cantidad[0]=int(input("Dime tu 1 numero: "))
menor=cantidad[0]
for i in range(1,numeros):
    cantidad[i]=int(input(f"Dime tu {i+1} numero: "))
    if cantidad[i]<menor:
        menor=cantidad[i]
print(f"De tus {len(cantidad)}, tu numero menor es {menor}")