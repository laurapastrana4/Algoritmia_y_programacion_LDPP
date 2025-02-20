Algoritmo Ejercicio_3_salario_y_comision
	//Entradas
	Escribir "Ingrese el valor de su sueldo base:$ "
	Leer sueldo_base
	Escribir "Ingrese el valor de la venta #1:$ "
	Leer venta1
	Escribir "Ingrese el valor de la venta #2:$ "
	Leer venta2
	Escribir "Ingrese el valor de la venta #3:$ "
	Leer venta3
	//caja negra
	total_ventas=(venta1+venta2+venta3)
	comision=0.10*total_ventas
	total=comision+sueldo_base
	//salidas
	Escribir "El total de su comision es:$ ",comision
	Escribir "El valor total que recibira es:$ ",total
FinAlgoritmo
