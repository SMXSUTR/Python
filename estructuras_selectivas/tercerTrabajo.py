valor= 0
pregunta= input("La empresa quiere comprar piezas pequellas de 50,000? Y/N: ")
if pregunta=="Y" or pregunta=="y":
    preguntaCantidad= int(input("cuantas piezas pequeñas deseas comprar? "))
    valor+=(preguntaCantidad*50000)
pregunta= input("La empresa quiere comprar piezas medianas de 100,000? Y/N: ")
if pregunta=="Y" or pregunta=="y":
    preguntaCantidad= int(input("cuantas piezas medianas deseas comprar? "))
    valor+=(preguntaCantidad*100000)
pregunta= input("La empresa quiere comprar piezas grandes de 200,000? Y/N: ")
if pregunta=="Y" or pregunta=="y":
    preguntaCantidad= int(input("cuantas piezas grandes deseas comprar? "))
    valor+=(preguntaCantidad*200000)
if valor>500000:
    valorEmpresa=valor*0.55
    valorBanco=valor*0.30
    creditoFabricante=valor*0.15
    print(f"Valor que paga con su propio dinero: {valorEmpresa}")
    print(f"Valor que paga el banco: {valorBanco}")
    print(f"Valor que paga a credito solicitado al fabricante: {creditoFabricante}")
else:
    valorEmpresa=valor*0.70
    creditoFabricante=valor*0.30
    conceptoInteres=creditoFabricante*0.20
    totalFabricante = creditoFabricante + conceptoInteres
    print(f"Valor que paga con su propio dinero: {valorEmpresa}")
    print(f"Valor que paga a credito solicitado al fabricante: {creditoFabricante}")
    print(f"Valor que cobra por concepto del credito solicitado al fabricante: {conceptoInteres}")
    print(f"Total a pagar al fabricante (con intereses): {totalFabricante}")