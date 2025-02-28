#Ejercicio_4_inversion_empresa
#Entrada
valor_compra = float(input("Ingrese el valor total de la compra: "))

#caja negra
if valor_compra > 5000000:
    inversion_propia = valor_compra * 0.55
    prestamo_banco = valor_compra * 0.30
    credito_fabricante = valor_compra * 0.15
    intereses_credito = credito_fabricante * 0.20
else:
    inversion_propia = valor_compra * 0.70
    prestamo_banco = 0  
    credito_fabricante = valor_compra * 0.30
    intereses_credito = credito_fabricante * 0.20

# salida
print(f"Cantidad a invertir de los fondos de la empresa: {inversion_propia:} COP")
print(f"Cantidad del crédito al fabricante: {credito_fabricante:} COP")
print(f"Valor de intereses: {intereses_credito:} COP")
if prestamo_banco > 0:
    print(f"Cantidad prestada del banco: {prestamo_banco:} COP")
else:
    print("Prestamo no es necesario.")