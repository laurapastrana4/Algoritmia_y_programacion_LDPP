Algoritmo Ejercicio_21_cuotas
	// Entradas
    Escribir "Ingrese el precio al contado: "
    Leer precio
    Escribir "Ingrese el valor de cada cuota: "
    Leer cuota
    // Caja negra
    costo_total_cuotas=cuota*12
    recargo=costo_total_cuotas-precio
    porcentaje_recargo=(recargo/precio)*100
    // Salidas
    Escribir "El porcentaje de recargo es: ", porcentaje_recargo, "%"
	
FinAlgoritmo
