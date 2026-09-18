stockBajo=int(input("Dime a partir de que numero la cantidad de stock es baja: "))
j=0
cantidad=int(input("Dime la cantidad de productos que quieres rectificar: "))
objetos=[0]*cantidad
stocks=[0]*cantidad
objetosBajos=[0]*cantidad
stocksBajos=[0]*cantidad
for i in range(cantidad):
    objetos[i]=input("Dime el nombre del producto: ")
    stocks[i]=int(input(f"Dime la cantidad de productos que tiene {objetos[i]}: "))
    if stocks[i]<=stockBajo:
        objetosBajos[j]=objetos[i]
        stocksBajos[j]=stocks[i]
        j+=1
for i in range(cantidad):
    print(f"Del producto {objetos[i]}, tiene {stocks[i]} en stock")
print(f"Tu stock bajo es desde {stockBajo} hacia abajo, entonces estos son los productos en stock bajo: ")
for i in range(j):
    print(f"Tu producto en stock bajo es {objetosBajos[i]}, teniendo {stocksBajos[i]} cantidad de productos")