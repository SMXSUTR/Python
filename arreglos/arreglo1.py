#Escribir y mostrar 5 numeros
numeros=[0]*5
for i in range(5):
    numeros[i]=float(input(f"Dime tu {i+1} numero: "))
for i in range(5):
    print(f"Tu {i+1} numero es, {numeros[i]}")