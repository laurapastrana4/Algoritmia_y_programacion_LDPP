#Entradas
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajas: "))
valor_por_hora = float(input("Ingrese el valor por hora trabajada: $ "))

#caja negra
salario_bruto = horas_trabajadas * valor_por_hora
descuento_por_impuesto = salario_bruto * 0.20
salario_neto = salario_bruto - descuento_por_impuesto

#salidas
print("Su salario neto es de: $ ",salario_neto)