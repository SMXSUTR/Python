#Escribir y sacar el promedio a 5 numeros
numeros=[0]*5
total=0
for i in range(5):
    numeros[i]=float(input(f"Dame tu {i+1} numero y sacare el promedio de los 5: "))
    total+=numeros[i]
print(f"Tu promedio seria {total/len(numeros)}")