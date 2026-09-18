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
print(f"Los estudiantes que consiguieron una nota entre 69 a 79 son {estudiantePromedio}")
print(f"Los estudiantes que consiguieron una nota entre 80 a 100 son {estudianteMejor}")