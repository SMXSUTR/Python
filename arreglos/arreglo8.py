#Guardar nombres y mostrarlos.  
cantidad=int(input("Dime la cantidad de nombres que quieres guardar: "))
nombres=[0]*cantidad
for i in range(cantidad):
    nombres[i]=input(f"Dime el {i+1} nombre")
for i in range(cantidad):
    print(f"El {i+1} nombre es {nombres[i]}")