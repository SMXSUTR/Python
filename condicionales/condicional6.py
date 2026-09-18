n1=float(input("Dime un tres y te dire cual es mayor de los tres: "))
n2=float(input("Dime un dos y te dire cual es mayor de los tres: "))
n3=float(input("Dime un uno y te dire cual es mayor de los tres: "))
if n1>n2:
    if n1>n3:
        print(f"El numero mayor de los tres, es el numero {n1}")
    else:
        print(f"El numero mayor de los tres, es el numero {n3}")
elif n2>n3:
    print(f"El numero mayor de los tres, es el numero {n2}")
else:
    print(f"El numero mayor de los tres, es el numero {n3}")