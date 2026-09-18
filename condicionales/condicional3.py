n1=int(input("Dime tu edad y te dire si eres un niño, un joven o un adulto: "))
if n1<=12:
    print(f"Si tu edad es {n1}, eres un niño")
elif n1>12 and n1<=20:
    print(f"Si tu edad es {n1}, eres un joven")
elif n1>20 and n1<60:
    print(f"Si tu edad es {n1}, eres un adulto")
else:
    print(f"tus {n1} años de edad no esta calibrado en nuestro archivo")