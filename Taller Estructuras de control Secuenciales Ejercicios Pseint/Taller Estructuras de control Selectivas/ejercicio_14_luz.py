#ejercicio_14_luz
# entradas
lectura_anterior = int(input("Ingrese la lectura anterior del medidor: "))
lectura_actual = int(input("Ingrese la lectura actual del medidor: "))

# caja negra
consumo = lectura_actual - lectura_anterior

monto = 0

if consumo <= 100:
    monto = consumo * 4600
elif consumo <= 300:
    monto = 100 * 4600 + (consumo - 100) * 80000
elif consumo <= 500:
    monto = 100 * 4600 + 200 * 80000 + (consumo - 300) * 100000
else:
    monto = 100 * 4600 + 200 * 80000 + 200 * 100000 + (consumo - 500) * 120000

#salidas
print(f"El monto a pagar por consumo de luz eléctrica es: {monto} COP")
