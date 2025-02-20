Algoritmo Ejercicio_18_interes_anual
	// Entrada
	Escribir "Ingrese el valor capital del prestamo: "
	Leer capital
	Escribir "Ingrese el valor de interes pagado: "
	Leer valor_interes
	Escribir "Ingrese el tiempo del prestamo en años: "
	Leer tiempo
	// caja negra
	tasa_anual=(valor_interes/(capital*tiempo))*100
	// salida
	Escribir "El porcentaje anual de interes es de: " tasa_anual, "%"
	FinAlgoritmo