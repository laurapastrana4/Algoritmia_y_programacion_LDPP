Algoritmo Ejercicio_11_trabajador
	//entradas
	Escribir "Ingrese su Nombre: "
	Leer nombre
	Escribir "Ingrese número de horas trabajadas: "
	Leer horas_normales_trabajadas
	Escribir "Ingrese el valor de la hora trabajada: "
	Leer valor_hora_trabajada
	Escribir "Ingrese cantidad de horas extras trabajadas: "
	Leer horas_extras
	Escribir "Ingrese la cantidad de hijos que tiene: "
	Leer cantidad_hijos
	//caja negra
	salario_base=horas_normales_trabajadas*valor_hora_trabajada
	pago_hora_extra=valor_hora_trabajada*1.25
	total_horas_extras=horas_extras*pago_hora_extra
	
	actualizacion_academica=250000
	asignacion_por_hijo=cantidad_hijos*173000
	prima_hogar=180000
	
	pago_forzoso=(salario_base)*0.05
	politica_habitacional=(salario_base)*0.02
	caja_ahorro=(salario_base)*0.07
	
	Sueldo_neto=(salario_base+total_horas_extras+actualizacion_academica+asignacion_por_hijo+prima_hogar)-(pago_forzoso+politica_habitacional+caja_ahorro)
	
	Escribir nombre " Su Salario neto es de: $ ", Sueldo_neto
FinAlgoritmo
