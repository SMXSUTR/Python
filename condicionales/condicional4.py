n1=int(input("Escribe el valor de tu pedido: ")) #si tu pedido es superior a los 100.000 entonces tendras un descuento del 20%
if n1>100000:
    print(f"Tu pedido de {n1} pesos, tuvo un descuento y ahora vale {n1*0.80}")
else:
    print(f"Tu pedido tiene un valor de {n1}")