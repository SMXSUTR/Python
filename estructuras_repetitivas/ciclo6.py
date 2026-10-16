while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
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
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")