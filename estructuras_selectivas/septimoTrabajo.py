cantidadLlantas= int(input("Dime cuantas llantas vas a comprar: "))
if cantidadLlantas<5 and cantidadLlantas>0:
    venta=cantidadLlantas*300000
elif cantidadLlantas>=5 and cantidadLlantas<=10:
    venta=cantidadLlantas*250000
elif cantidadLlantas>10:
    venta=cantidadLlantas*200000
print(f"Cada llanta vale {venta/cantidadLlantas}, quiere {cantidadLlantas}, y el valor total es de {venta}")