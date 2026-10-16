porcentajeEmoglobina = float(input("Dime el número de tu porcentaje de hemoglobina: "))
sexo = input("Eres hombre o mujer? H/M: ").lower()
tipoEdad = input("Dime si tu edad es por años o meses A/M: ").lower()

if tipoEdad == "m":
    meses = int(input("Dime cuántos meses tienes: "))
    if meses >= 0 and meses <= 1:
        if porcentajeEmoglobina < 13:
            print("positivo (anemia)")
        elif 13 <= porcentajeEmoglobina <= 26:
            print("negativo")
        else:
            print("exceso de hemoglobina")
    elif meses > 1 and meses <= 6:
        if porcentajeEmoglobina < 10:
            print("positivo (anemia)")
        elif 10 <= porcentajeEmoglobina <= 18:
            print("negativo")
        else:
            print("exceso de hemoglobina")
    elif meses > 6 and meses <= 12:
        if porcentajeEmoglobina < 11:
            print("positivo (anemia)")
        elif 11 <= porcentajeEmoglobina <= 15:
            print("negativo")
        else:
            print("exceso de hemoglobina")

elif tipoEdad == "a":
    años = int(input("Dime cuántos años tienes: "))
    if años > 1 and años <= 5:
        if porcentajeEmoglobina < 11.5:
            print("positivo (anemia)")
        elif 11.5 <= porcentajeEmoglobina <= 15:
            print("negativo")
        else:
            print("exceso de hemoglobina")
    elif años > 5 and años <= 10:
        if porcentajeEmoglobina < 12.6:
            print("positivo (anemia)")
        elif 12.6 <= porcentajeEmoglobina <= 15.5:
            print("negativo")
        else:
            print("exceso de hemoglobina")
    elif años > 10 and años <= 15:
        if porcentajeEmoglobina < 13:
            print("positivo (anemia)")
        elif 13 <= porcentajeEmoglobina <= 15.5:
            print("negativo")
        else:
            print("exceso de hemoglobina")
    elif años > 15:
        if sexo == "m":  # mujer
            if porcentajeEmoglobina < 12:
                print("positivo (anemia)")
            elif 12 <= porcentajeEmoglobina <= 16:
                print("negativo")
            else:
                print("exceso de hemoglobina")
        elif sexo == "h":  # hombre
            if porcentajeEmoglobina < 14:
                print("positivo (anemia)")
            elif 14 <= porcentajeEmoglobina <= 18:
                print("negativo")
            else:
                print("exceso de hemoglobina")
