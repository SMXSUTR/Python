zapatillasBlancas=20000
zapatillasNegras=30000
zapatillasAzules=40000
i=0
cantidadPedido= int(input("Un pedido de cuantas unidades te gustaria hacer? "))
while i<cantidadPedido:
    pedido= int(input("Cual zapatillas te gustaria elegir? 1) Zapatillas blancas (20,000) 2) Zapatillas negras (30,000) 3) Zapatillas azules (40,0000)"))
    if pedido==1:
        cantidadBlancos= int(input("Dime la cantidad de Zapatos blancos que quieres comprar:"))
        totalB=cantidadBlancos*zapatillasBlancas
        i+=cantidadBlancos
    elif pedido==2:
        cantidadNegros= int(input("Dime la cantidad de Zapatos negros que quieres comprar:"))
        totalN=cantidadNegros*zapatillasNegras
        i+=cantidadNegros
    else:
        cantidadAzules= int(input("Dime la cantidad de Zapatos azules que quieres comprar:"))
        totalA=cantidadAzules*zapatillasAzules
        i+=cantidadAzules
if cantidadPedido>=3:
    total=(totalB+totalN+totalA)
    print(f"El valor de los {cantidadPedido} productos, es de {total}")
    print(f"El valor del descuento es de {total*0.20}")
    print(f"El valor a pagar es de {total-(total*0.20)}")
else:
    total=(totalB+totalN+totalA)
    print(f"El valor de los {cantidadPedido} productos, es de {total}")
    print(f"El valor del descuento es de {total*0.10}")
    print(f"El valor a pagar es de {total-(total*0.10)}")