Algoritmo Ejercicio_9_salario_neto
	//Entradas
	Escribir "Ingrese la cantidad de horas trabajadas: "
	Leer horas_trabajadas
	Escribir "Ingrese el valor por hora trabajada: $ "
	Leer valor_por_hora
	//caja negra
	salario_bruto=horas_trabajadas*valor_por_hora
	descuento_por_impuesto=salario_bruto*0.20
	salario_neto=salario_bruto-descuento_por_impuesto
	//salidas
	Escribir "Su salario neto sería: $ ", salario_neto
	
FinAlgoritmo
