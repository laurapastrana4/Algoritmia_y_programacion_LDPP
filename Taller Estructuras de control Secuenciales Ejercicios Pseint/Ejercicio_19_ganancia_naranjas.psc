Algoritmo Ejercicio_19_ganancia_naranjas
	//entradas
	Escribir "Ingrese el numero de naranjas: "
	leer cantidad_naranjas
	Escribir "Ingrese el precio por docena: "
	leer precio_docena
	Escribir "Ingrese el valor total de ingresos: "
	Leer valor_total_ingresos
	//caja negra
	costo_total=(cantidad_naranjas*precio_docena)/12
	ganancia_total=valor_total_ingresos-costo_total
	porcentaje_ganancia=(ganancia_total/costo_total)*100
	//salidas
	Escribir "El porcentaje de ganancia obtenida en la inversión es de: ", porcentaje_ganancia "%"

FinAlgoritmo
