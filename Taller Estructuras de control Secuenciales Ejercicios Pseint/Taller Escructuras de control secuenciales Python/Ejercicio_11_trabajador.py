#Entradas
nombre = str(input("Ingrese su nombre: "))
horas_normales_trabajadas = float(input("Ingrese número de horas trabajadas: "))
valor_hora_trabajada = float(input("ingrese el valor de la hora trabajada: "))
horas_extras = float(input("Ingrese la cantidad de horas extras trabajadas: "))
cantidad_hijos = int(input("Ingrese la cantidad de hijos que tiene: "))

#caja negra
salario_base = horas_normales_trabajadas * valor_hora_trabajada
pago_hora_extra = valor_hora_trabajada * 1.25
total_horas_extras=horas_extras * pago_hora_extra
	
actualizacion_academica = 250000
asignacion_por_hijo=cantidad_hijos * 173000
prima_hogar = 180000
	
pago_forzoso = (salario_base) * 0.05
politica_habitacional = (salario_base) * 0.02
caja_ahorro = (salario_base) * 0.07
	
Sueldo_neto = (salario_base + total_horas_extras + actualizacion_academica + asignacion_por_hijo + prima_hogar) - (pago_forzoso + politica_habitacional + caja_ahorro)

#salidas
print(nombre,",Su salario neto es de: $ ",Sueldo_neto)