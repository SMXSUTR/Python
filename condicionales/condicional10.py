n1=int(input("Dame tu nota y te dare tu resultado: "))
if n1>7 and n1<11:
    print("Tu calificacion es A")
elif n1>5 and n1<8:
    print("Tu calificacion es B")
elif n1>0 and n1<6:
    print("Tu calificacion es C")
else:
    print("Error, fuera de parametros")