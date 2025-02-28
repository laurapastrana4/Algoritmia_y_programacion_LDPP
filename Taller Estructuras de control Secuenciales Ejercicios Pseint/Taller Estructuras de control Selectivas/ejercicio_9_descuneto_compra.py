#Ejercicio_9_descuneto_compra
# Entradas
nombre_cliente = input("Ingrese el nombre del cliente: ")
valor_compra = float(input("Ingrese el valor de la compra en COP: "))

# Caja negra
if (valor_compra < 50000):
    descuento = 0.0
elif (valor_compra > 50000 and valor_compra <= 100000):
    descuento = 0.05
elif (valor_compra > 100000 and valor_compra <= 700000):
    descuento = 0.11
elif (valor_compra > 700000 and valor_compra <= 1500000):
    descuento = 0.18
elif (valor_compra > 1500000):
    descuento = 0.25

valor_descuento = valor_compra * descuento
valor_a_pagar = valor_compra - valor_descuento

# Salida
print(f"Nombre del cliente: {nombre_cliente}")
print(f"Valor de la compra: {valor_compra:,} COP")
print(f"Descuento recibido: {valor_descuento:,} COP
print(f"Valor a pagar: {valor_a_pagar:,} COP")
