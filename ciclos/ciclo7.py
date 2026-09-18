numeroAutos=int(input("Dame el numero de autos que entraron a ibague en esta dia/semana/mes/año y te dire su color de placa"))
for i in range(1, numeroAutos+1):
    placa=int(input("Dame el ultimo digito de la placa del auto: "))
    if placa==1 or placa==2:
        print("su color de calcomania es amarillo")
    elif placa==3 or placa==4:
        print("su color de calcomania es rosa")
    elif placa==5 or placa==6:
        print("su color de calcomania es roja")
    elif placa==7 or placa==8:
        print("su color de calcomania es verde")
    elif placa==9 or placa==0:
        print("su color de calcomania es azul")
    else:
        print("Este dato no esta guardado en la base de datos, solo se resive un digito")