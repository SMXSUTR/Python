while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        estudiantePeor=0
        estudianteIntermedio=0
        estudiantePromedio=0
        estudianteMejor=0
        for i in range(1, 24):
            estudiante=int(input(f"Dime la nota del estudiante numero {i}"))
            if estudiante>=1 and estudiante<50:
                estudiantePeor+=1
            elif estudiante>=50 and estudiante<70:
                estudianteIntermedio+=1
            elif estudiante>=70 and estudiante<80:
                estudiantePromedio+=1
            elif estudiante>=80 and estudiante<=100:
                estudianteMejor+=1
            else:
                print(f"El puntaje {estudiante}, no entra e el rango")
        print(f"Los estudiantes que consiguieron una nota entre 1 a 49 son {estudiantePeor}")
        print(f"Los estudiantes que consiguieron una nota entre 50 a 69 son {estudianteIntermedio}")
        print(f"Los estudiantes que consiguieron una nota entre 70 a 79 son {estudiantePromedio}")
        print(f"Los estudiantes que consiguieron una nota entre 80 a 100 son {estudianteMejor}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")