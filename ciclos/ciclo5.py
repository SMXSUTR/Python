promedioNiños=0
promedioJovenes=0
promedioAdultos=0
promedioAncianos=0
niños=0
jovenes=0
adultos=0
ancianos=0
for i in range(1, 51):
    edad=int(input(f"Dime la edad de la {i} persona: "))
    peso=float(input(f"Dime el peso de la {i} persona: "))
    if edad>=0 and edad<=12:
        niños+=1
        promedioNiños+=peso
    elif edad>=13 and edad<=29:
        jovenes+=1
        promedioJovenes+=peso
    elif edad>=30 and edad<=59:
        adultos+=1
        promedioAdultos+=peso
    elif edad>=60:
        ancianos+=1
        promedioAncianos+=peso
if niños > 0:
    print(f"La cantidad de niños es {niños}, y el promedio de pesos es {promedioNiños/niños}")
else:
    print("No se ingresaron niños.")
if jovenes > 0:
    print(f"La cantidad de jóvenes es {jovenes}, y el promedio de pesos es {promedioJovenes/jovenes}")
else:
    print("No se ingresaron jóvenes.")
if adultos > 0:
    print(f"La cantidad de adultos es {adultos}, y el promedio de pesos es {promedioAdultos/adultos}")
else:
    print("No se ingresaron adultos.")
if ancianos > 0:
    print(f"La cantidad de ancianos es {ancianos}, y el promedio de pesos es {promedioAncianos/ancianos}")
else:
    print("No se ingresaron ancianos.")