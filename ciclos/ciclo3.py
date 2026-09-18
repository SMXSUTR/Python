menor=100
mayor=0
promedio=0
for i in range(1,21):
    numero=int(input(f"Dame la nota del {i} estudiante (Rango 1-100)"))
    promedio+=numero
    if numero<0 or numero>100:
        print("Tu resultado saldra erroneo (nota fuera de rango)")
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor=numero
promedio/=20
print(f"Tu nota mayor es de {mayor}")
print(f"Tu nota menor es de {menor}")
print(f"Tu nota promedio es de {promedio}")