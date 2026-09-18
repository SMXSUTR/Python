numero=int(input("Dime el numero de personas en el grupo de alumnos: "))
mujeres=0
hombres=0
edadH=0
edadM=0
for i in range(1, numero+1):
    persona=input("Eres homre o mujer? H/M: ")
    edad=int(input("Dime tu edad: "))
    if persona=="H" or persona=="h":
        hombres+=1
        edadH+=edad
    elif persona=="M" or persona=="m":
        mujeres+=1
        edadM+=edad
print(f"El numero de hombres es de {hombres} y el promedio de edad es de {edadH/hombres}")
print(f"El numero de mujeres es de {mujeres} y el promedio de edad es de {edadM/mujeres}")