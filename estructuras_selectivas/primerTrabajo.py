NumeroUno= int(input("Para darte tu promedio y ver si aprobaste o no dame tu primer numero: "))
NumeroDos= int(input("Para darte tu promedio y ver si aprobaste o no dame tu segundo numero: "))
NumeroTres= int(input("Para darte tu promedio y ver si aprobaste o no dame tu tercer numero: "))
promedio= (NumeroUno+NumeroDos+NumeroTres)/3
if promedio<70:
    print(f"Tu promedio es {promedio}, desaprobaste")
else:
    print(f"Tu promedio es {promedio}, aprobaste")