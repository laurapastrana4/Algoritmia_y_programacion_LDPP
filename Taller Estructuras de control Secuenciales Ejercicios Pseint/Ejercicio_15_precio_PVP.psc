Algoritmo Ejercicio_15_precio_PVP
	//entradas
	Escribir "Ingrese el valor final pagado por el producto: "
	Leer valor_final_pagado
	Escribir "Ingrese el PVP, precio de venta al publico: "
	Leer precio_venta_publico
	//caja negra
	valor_descuento=precio_venta_publico-valor_final_pagado
	divisi�n=valor_descuento/precio_venta_publico
	porcentaje=divisi�n*100
	//salidas
	Escribir "El porcentaje de descuento es de: ", porcentaje "%"
FinAlgoritmo
