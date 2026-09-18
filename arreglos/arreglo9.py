cantidad =int(input("Dime la cantidad de numeros que quieres guardar: "))
numeros =[0]*cantidad
for i in range(cantidad):
    numeros[i]=int(input(f"Dime tu {i+1} numero: "))
for i in range(cantidad):
    for j in range(i+1, cantidad):
        if numeros[i] > numeros[j]:
            guardado = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = guardado
print("Números ordenados:")
for i in range(cantidad):
    print(f"{i+1} numero: {numeros[i]}")
