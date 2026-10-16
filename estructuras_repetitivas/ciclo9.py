while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        numero=int(input("Dime el numero de personas en el grupo de alumnos: "))
        mujeres=0
        hombres=0
        edadH=0
        edadM=0
        if numero>=1:
            for i in range(1, numero+1):
                persona=input("Eres homre o mujer? H/M: ")
                edad=int(input("Dime tu edad: "))
                if (persona=="H" or persona=="h") or (persona=="M" or persona=="m"):
                    if persona=="H" or persona=="h":
                        hombres+=1
                        edadH+=edad
                    elif persona=="M" or persona=="m":
                        mujeres+=1
                        edadM+=edad
                else:
                    print("Error, el sexo que nos diste no nos sirve para este proceso")
        else:
            print("Error, el numero de no nos sirve para este proceso")
        if hombres > 0:
            print(f"El número de hombres es {hombres} y el promedio de edad es {edadH/hombres}")
        else:
            print("No se ingresaron hombres")
        if mujeres > 0:
            print(f"El número de mujeres es {mujeres} y el promedio de edad es {edadM/mujeres}")
        else:
            print("No se ingresaron mujeres")
        if hombres + mujeres > 0:
            print(f"Promedio general del grupo: {(edadH+edadM)/(hombres+mujeres)}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")