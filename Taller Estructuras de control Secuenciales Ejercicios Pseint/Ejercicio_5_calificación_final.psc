Algoritmo Ejercicio_5_calificación_final
	//Entradas
	Escribir "Su calificación final de Cómputo se compone por: "
	Escribir "55% de promedio de parciales, 30% de examen final y 15% de trabajo final"
	
	Escribir "Ingrese su nota 1: "
	Leer nota1
	Escribir "Ingrese su nota 2: "
	Leer nota2
	Escribir "Ingrese su nota 3: "
	Leer nota3
	Escribir "Ingrese su calificación del examen final: "
	Leer examen_final
	Escribir "Ingrese su calificación del trabajo final: "
	Leer trabajo_final
	//caja negra
	promedio_notas=(nota1+nota2+nota3)/3
	porcentaje_notas=promedio_notas*0.55
	porcentaje_examen=examen_final*0.30
	porcentaje_trabajo=trabajo_final*0.15
	calificación_final=porcentaje_examen+porcentaje_notas+porcentaje_trabajo
	//salidas
	Escribir "Su calificación final de Cómputo es de: ", calificación_final
	
FinAlgoritmo
