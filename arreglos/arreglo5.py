#Buscar un número en el arreglo.  
numeros=int(input("Dime el numero de entidades que evaluaremos: "))
cantidad=[0]*numeros
for i in range(numeros):
    cantidad[i]=int(input(f"Estamos en el numero {i+1}, dime el numero que guardaras: "))
buscar=int(input("Dime el numero que buscas"))
encontrado=False
for i in range(numeros):
    if cantidad[i]==buscar:
        print(f"Tu numero {buscar} es el numero {i}")
        encontrado=True
        break
if not encontrado:
    print(f"El numero no fue encontrado en la base de datos")