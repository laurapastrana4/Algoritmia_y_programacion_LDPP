Algoritmo Ejercicio_8
	//Entradas
	Escribir "Ingrese su calificación: "
	leer cal
	
	//caja negra
	si cal >= 90 Entonces
		escribir "A"
	sino 
		Si cal >= 80 y cal < 90 Entonces
			escribir "B"
			SiNo
				si cal >= 70 y cal < 80 Entonces
					escribir "C"
				sino 
					si cal >= 60 y cal < 70 Entonces
						Escribir "D"
					SiNo
						si cal < 60 Entonces
							Escribir "F"
						FinSi
					FinSi
				FinSi
		FinSi
	FinSi
	

FinAlgoritmo
