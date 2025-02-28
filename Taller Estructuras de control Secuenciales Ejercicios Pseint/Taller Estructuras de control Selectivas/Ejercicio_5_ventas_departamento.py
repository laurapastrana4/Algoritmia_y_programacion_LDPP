#Ejercicio_5_ventas_departamento
# Entradas
ventas_depto1 = float(input("Ingrese el total de las ventas del departamento 1: "))
ventas_depto2 = float(input("Ingrese el total de las ventas del departamento 2: "))
ventas_depto3 = float(input("Ingrese el total de las ventas del departamento 3: "))
salario_mensual = float(input("Ingrese el salario mensual de un vendedor: "))

# Caja negra
ventas_totales = ventas_depto1 + ventas_depto2 + ventas_depto3

base_ventas = 0.33 * ventas_totales

if ventas_depto1 > base_ventas:
    incentivo_depto1 = salario_mensual * 0.20
else:
    incentivo_depto1 = 0
salario_final_depto1 = salario_mensual + incentivo_depto1

if ventas_depto2 > base_ventas:
    incentivo_depto2 = salario_mensual * 0.20
else:
    incentivo_depto2 = 0
salario_final_depto2 = salario_mensual + incentivo_depto2

if ventas_depto3 > base_ventas:
    incentivo_depto3 = salario_mensual * 0.20
else:
    incentivo_depto3 = 0
salario_final_depto3 = salario_mensual + incentivo_depto3

# Salida
print(f"El sueldo final de los vendedores del departamento 1 es: {salario_final_depto1} COP")
print(f"El sueldo final de los vendedores del departamento 2 es: {salario_final_depto2} COP")
print(f"El sueldo final de los vendedores del departamento 3 es: {salario_final_depto3} COP")
