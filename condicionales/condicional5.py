n1=int(input("Dime tu nota (del 1 al 100) y te dire si aprobaste o no: "))
if n1>=60:
    print(f"Aprobaste con {n1}")
elif n1>0 and n1<70:
    print(f"Reprobaste con {n1}")
else:
    print(f"error")