import random
balota= random.choice(["rojo", "verde", "azul", "negro"])
valor= int(input("Dime el valor de tu compra: "))
if balota=="rojo":
    print(f"FELICIDADES! Conseguiste una balota roja, tu descuento del 15% restando {valor*0.15} a tu costo de {valor}, ahora tu compra solo costara {valor*0.85}")
elif balota=="verde":
    print(f"FELICIDADES! Conseguiste una balota verde, tu descuento del 20% restando {valor*0.20} a tu costo de {valor}, ahora tu compra solo costara {valor*0.80}")
elif balota=="azul":
    print(f"Lo sentimos, sacaste una valota azul, no ganaste un descuento, tu compra sale en {valor}")
else:
    print(f"Lo sentimos, sacaste una valota negra, no ganaste un descuento, tu compra sale en {valor}") 