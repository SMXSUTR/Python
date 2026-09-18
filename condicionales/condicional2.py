n1=float(input("Dime tu primer numero y te dire cual es el mayor y cual es menor: "))
n2=float(input("Dime tu segundo numero y te dire cual es el mayor y cual es menor: "))
if n1>n2:
    print(f"{n1} es mayor que {n2}")
elif n1==n2: 
    print(f"{n1} y {n2} son iguales")
else:
    print(f"{n2} es mayor que {n1}")