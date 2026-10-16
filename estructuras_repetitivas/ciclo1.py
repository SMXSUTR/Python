positivo=0
negativo=0
neutro=0
for i in range(1, 21):
    numeros=float(input(f"dime tu {i} numero, negativo, positivo o neutral: "))
    if numeros>0:
        positivo+=1
    elif numeros<0:
        negativo+=1
    else:
        neutro+=1
print(f"Nos da un total de {positivo} numero/s positivos")
print(f"Nos da un total de {negativo} numero/s negativos")
print(f"Nos da un total de {neutro} numero/s neutros")