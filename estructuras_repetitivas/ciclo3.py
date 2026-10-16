while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        menor=100
        mayor=0
        promedio=0
        contador=0
        for i in range(1,21):
            numero=int(input(f"Dame la nota del {i} estudiante (Rango 1-100)"))
            if numero>0 and numero<=100:
                promedio+=numero
                contador+=1
                if numero>mayor:
                    mayor=numero
                if numero<menor:
                    menor=numero
            else:
                print("Tu resultado saldra erroneo (nota fuera de rango)")
                continue
        promedio/=contador
        print(f"Tu nota mayor es de {mayor}")
        print(f"Tu nota menor es de {menor}")
        print(f"Tu nota promedio es de {promedio}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")