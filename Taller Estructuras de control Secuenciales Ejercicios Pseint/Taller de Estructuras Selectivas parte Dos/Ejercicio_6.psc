Algoritmo Ejercicio_6
	//Entradas
	Escribir "Ingrese a�o: "
	leer year

	//Caja negra
	si year mod 4=0 y year mod 100<>1 o year mod 400=0
		Entonces
		escribir "Es bisiesto"
	SiNo
		Escribir "No es bisiesto"
	FinSi
FinAlgoritmo
