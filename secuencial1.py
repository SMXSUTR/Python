salarioMinimo=int(input("Dime el valor de tu salario (salario minimo:2000000):"))
diasMes=30
salarioDiario=salarioMinimo/diasMes
diasTrabajados=int(input("Dime los dias que trabajas en el mes: "))
valorDias=salarioDiario*diasTrabajados 
print(f"Tu salario calculado segun tus dias trabajados es de ${valorDias:,.0f}COP")