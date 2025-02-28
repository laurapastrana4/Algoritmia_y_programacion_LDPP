#Ejercicio_2_incremento_sueldo
# Entrada
sueldo = float(input("Ingrese el sueldo del trabajador: "))

# Caja negra
if sueldo < 900000:
    incremento = sueldo * 0.15
else:
    incremento = sueldo * 0.12

sueldo_total = sueldo + incremento

# Salida
print(f"El nuevo sueldo del trabajador es: {sueldo_total} COP")