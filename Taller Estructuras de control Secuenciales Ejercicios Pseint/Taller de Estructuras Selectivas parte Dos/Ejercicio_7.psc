Algoritmo Ejercicio_7
	//Entradas
	Escribir "Ingrese numero: "
	leer num
	contador = 0
	Para i = 1 Hasta num Hacer
		si num % i = 0 Entonces
			contador=contador+1
		FinSi
	FinPara
	Si contador = 2 Entonces
		Escribir num " es un número primo"
	sino 
		Escribir num " no es un número primo"
	FinSi
FinAlgoritmo
