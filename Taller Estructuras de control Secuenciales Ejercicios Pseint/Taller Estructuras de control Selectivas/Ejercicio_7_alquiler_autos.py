#Ejercicio_7_alquiler_autos
# Entradas
distancia_recorrida = float(input("Ingrese la distancia recorrida en kilómetros: "))

# Caja negra
if distancia_recorrida <= 300:
    pago = 50000
elif 300 < distancia_recorrida < 1000:
    pago = 70000 + 30000 * (distancia_recorrida - 300)
else:
    pago = 150000 + 9000 * (distancia_recorrida - 1000)

# Salida
print(f"El monto a pagar por el cliente es: {pago} COP")
