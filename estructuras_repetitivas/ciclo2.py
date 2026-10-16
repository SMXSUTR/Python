for i in range(1, 11):
    numero=int(input(f"Dime tu {i} numero"))
    if numero<0:
        negativo=(numero*-1)
        suma+=negativo
        print(f"Tu numero se convirtio a {negativo}")
print(f"la suma de todos los negaivos combertidos a positivos es {suma}")