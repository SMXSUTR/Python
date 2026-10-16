# Programa modificado a partir del ejercicio de las llantas
# Ahora sirve para evaluar el resultado académico de un estudiante
notaFinal = float(input("Dime tu nota final (0 a 5): "))
# Condiciones cambiadas por completo
if notaFinal < 3.0 and notaFinal >= 0:
    resultado = "Reprobado"
elif notaFinal >= 3.0 and notaFinal <= 4.0:
    resultado = "Aprobado"
elif notaFinal > 4.0 and notaFinal <= 5.0:
    resultado = "Aprobado con excelencia"
else:
    resultado = "Nota inválida"
print(f"Tu nota es {notaFinal} y tu resultado es: {resultado}")