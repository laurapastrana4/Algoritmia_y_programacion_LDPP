Algoritmo Ejercicio_9
	//Entradas
	Escribir "Ingrese número: "
	leer num
	long=Longitud(num)
	inversa=""
	Para i<-long Hasta 1 Con Paso -1 Hacer
		inversa = inversa+Subcadena(num,i,i)
	Fin Para
	Escribir inversa
	Si num = inversa entonces
		Escribir  "Es un palindromo"
	sino 
		Escribir  "No es un palindromo"
	FinSi
FinAlgoritmo
