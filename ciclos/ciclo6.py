hombres=0
mujeres=0
numeroEstudiantes=int(input("Dime la cantidad de estudiantes ddentro de el salon: "))
for i in range(1, numeroEstudiantes+1):
    tipoEstudiante=input(f"El estudiante numero {i} es hombre o mujer? M/H: ")
    if tipoEstudiante=="H" or tipoEstudiante=="h":
        hombres+=1
    elif tipoEstudiante=="M" or tipoEstudiante=="m":
        mujeres+=1
    else:
        print(f"error ({tipoEstudiante}) no es un valor valido")
print(f"De {numeroEstudiantes}, {hombres} estudiantes son hombres y {mujeres} son mujeres")