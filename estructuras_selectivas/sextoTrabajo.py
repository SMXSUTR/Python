pension=3000000
periodoUno= int(input("Dime tu promedio del primer periodo: "))
periodoDos= int(input("Dime tu promedio del segundo periodo: "))
periodoTres= int(input("Dime tu nota en este ultimo periodo: "))
ultimoPromedio= (periodoUno+periodoDos+periodoTres)/3
if ultimoPromedio>=4 and ultimoPromedio<=5:
    pension*=0.70
elif ultimoPromedio<=4 and ultimoPromedio>=0:
    pension*=1.10
print(f"Tu promedio es de {ultimoPromedio} y tu precio de tu pension es de {pension}")