genero= input("Eres hombre o eres una mujer? H/M")
if genero=="H" or genero=="h":
    edad= int(input("Dime tu edad ahora: "))
    numeroPulsaciones=(210-edad)/10
else:
    edad= int(input("Dime tu edad ahora: "))
    numeroPulsaciones=(220-edad)/10
print(f"tu numero de pulsaciones {numeroPulsaciones}")