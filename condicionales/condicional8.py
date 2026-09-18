#IMPUESTO DEL SALARIO
n1=int(input("Dime cual es tu salario: "))
if n1>2000000:
    print(f"Tu salario de {n1}, con sus impuestos cobrados serian {n1*0.84}")
else:
    print(f"Tu salario de {n1}, no tiene impuesto")