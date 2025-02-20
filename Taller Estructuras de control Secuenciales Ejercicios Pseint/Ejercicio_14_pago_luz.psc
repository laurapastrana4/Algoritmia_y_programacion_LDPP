Algoritmo Ejercicio_14_pago_luz
	//Entradas
	Escribir "Ingrese el monto de la lectura anterior: "
	Leer lectura_anterior
	Escribir "Ingrese el monto de la lectura actual: "
	Leer lectura_actual
	Escribir "Ingrese el costo por kilovaltio: "
	leer costo_kilovaltio
	// caja negra
	montototal=(lectura_actual-lectura_anterior)*costo_kilovaltio
	// salidas
	Escribir "El monto total a pagar es de: " , montototal
	
FinAlgoritmo