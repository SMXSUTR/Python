conteo=0
edad=1
alturaPromedio=0
hombre=0
mujer=0
alturaMayor=0
alturaMenor=0
while True:
    edad=int(input(f"Estamos en el {conteo+1} estudiante, dime la edad del estudiante"))
    if edad==0:
        break
    conteo+=1
    sexo=input("Es homre o mujer? H/M: ")
    if sexo=="H" or sexo=="h":
        hombre+=1
    elif sexo=="M" or sexo=="m":
        mujer+=1
    else:
        print(f"No tenemos la variable {sexo}, en nuestra pagina")
    altura=float(input("Dime la altura de este estudiante(En metros): "))
    alturaPromedio+=altura
    if altura<=1.50:
        alturaMenor+=1
    elif altura>1.70:
        alturaMayor+=1
print(f"La cantidad de estudiantes es de {conteo}, la cantidad de hombres dentro de {conteo} es de: {hombre}")
print(f"La cantidad de mujeres es de: {mujer}")
if conteo>0:
    print(f"La altura promedio es de {alturaPromedio/conteo}")
else:
    print(f"La altura promedio es {alturaPromedio}")
print(f"La cantidad de alumnos que tienen una altura mayor a 1.70m es de: {alturaMayor}")
print(f"La cantidad de alumnos que tienen una altura menor o igual a 1.50m es de: {alturaMenor}")