# Entradas
sueldo_base = float(input("Ingrese el valor de su sueldo base:$ "))
venta1 = float(input("Ingrese el valor de la venta #1:$ "))
venta2 = float(input("Ingrese el valor de la venta #2:$ "))
venta3 = float(input("Ingrese el valor de la venta #3:$ "))

# Caja negra
total_ventas = venta1 + venta2 + venta3
comision = 0.10 * total_ventas
total = comision + sueldo_base

# Salidas
print("El total de su comision es:$", comision)
print("El valor total que recibira es:$", total)
