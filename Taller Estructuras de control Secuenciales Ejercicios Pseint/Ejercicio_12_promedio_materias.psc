Algoritmo Ejercicio_12_promedio_materias
	Escribir "Ingrese su calificaci�n del examen final de matem�ticas: "
	Leer examen_matematicas
	Escribir "Ingrese la nota de la nota 1 de matem�ticas: "
	Leer nota_1_math
	Escribir "Ingrese la nota de la nota 2 de matem�ticas: "
	Leer nota_2_math
	Escribir "Ingrese la nota de la nota 3 de matem�ticas: "
	Leer nota_3_math
	
	Escribir "Ingrese su calificaci�n del examen final de f�sica: "
	Leer examen_fisica
	Escribir "Ingrese la nota de la nota 1 de fisica: "
	Leer nota_1_fisica
	Escribir "Ingrese la nota de la nota 2 de fisica: "
	Leer nota_2_fisica
	
	Escribir "Ingrese su calificaci�n del examen final de qu�mica: "
	Leer examen_quimica
	Escribir "Ingrese la nota de la nota 1 de qu�mica: "
	Leer nota_1_quimica
	Escribir "Ingrese la nota de la nota 2 de qu�mica: "
	Leer nota_2_quimica
	Escribir "Ingrese la nota de la nota 3 de qu�mica: "
	Leer nota_3_quimica
	//caja negra
	promedio_nota_matematicas=(nota_1_math+nota_2_math+nota_3_math)/3
	porcentaje_nota_matematicas=promedio_nota_matematicas*0.10
	porcentaje_examen_matematicas=examen_matematicas*0.90
	nota_final_matematicas=porcentaje_examen_matematicas+porcentaje_nota_matematicas
	
	promedio_nota_fisica=(nota_1_fisica+nota_2_fisica)/2
	porcentaje_nota_fisica=promedio_nota_fisica*0.20
	porcentaje_examen_fisica=examen_fisica*0.80
	nota_final_fisica=porcentaje_examen_fisica+porcentaje_nota_fisica
	
	promedio_nota_quimica=(nota_1_quimica+nota_2_quimica+nota_3_quimica)/3
	porcentaje_nota_quimica=promedio_nota_quimica*0.15
	porcentaje_examen_quimica=examen_quimica*0.85
	nota_final_quimica=porcentaje_examen_quimica+porcentaje_nota_quimica
	
	promedio_general_3_materias=(nota_final_fisica+nota_final_matematicas+nota_final_quimica)/3
	
	//salidas
	Escribir "Su nota final de matem�ticas es de: ", nota_final_matematicas
	Escribir "Su nota final de fisica es de: ", nota_final_fisica
	Escribir "Su nota final de quimica es de: ", nota_final_quimica
	Escribir "El promedio de las 3 materias es de: ", promedio_general_3_materias
	
	
FinAlgoritmo
