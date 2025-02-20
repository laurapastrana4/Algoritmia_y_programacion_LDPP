Algoritmo Ejercicio_8_area_triangulo
	//entradas
	escribir "Ingrese la longitud lado A: "
	leer lado_a
	Escribir "Ingrese la longitud lado B: "
	leer lado_b
	Escribir "Ingrese la Longitud lado C: " 
	leer lado_c
	
	// caja negra
	S=(lado_a+lado_c+lado_c)/2
	area=Raiz(S*(S-lado_a)*(S-lado_b)*(S-lado_c))
	//salidas
	Escribir "El área del triángulo es: ", area
	
FinAlgoritmo