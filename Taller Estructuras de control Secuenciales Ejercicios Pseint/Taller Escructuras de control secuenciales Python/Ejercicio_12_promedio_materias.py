#Entradas
examen_matematicas = float(input("Ingrese su calificación del examen final de matemáticas: "))
nota_1_math = float(input("Ingrese la nota de la nota 1 de matemáticas: "))
nota_2_math = float(input("Ingrese la nota de la nota 2 de matemáticas: "))
nota_3_math = float(input("Ingrese la nota de la nota 3 de matemáticas: "))

examen_fisica = float(input("Ingrese su calificación del examen final de física: "))
nota_1_fisica = float(input("Ingrese la nota de la nota 1 de física: "))
nota_2_fisica = float(input("Ingrese la nota de la nota 2 de física: "))

examen_quimica = float(input("Ingrese su calificación del examen final de química: "))
nota_1_quimica = float(input("Ingrese la nota de la nota 1 de química: "))
nota_2_quimica = float(input("Ingrese la nota de la nota 2 de química: "))
nota_3_quimica = float(input("Ingrese la nota de la nota 3 de química: "))

#caja negra
promedio_nota_matematicas = (nota_1_math + nota_2_math +nota_3_math) / 3
porcentaje_nota_matematicas = promedio_nota_matematicas * 0.10
porcentaje_examen_matematicas = examen_matematicas * 0.90
nota_final_matematicas = porcentaje_examen_matematicas + porcentaje_nota_matematicas
	
promedio_nota_fisica = (nota_1_fisica + nota_2_fisica) / 2
porcentaje_nota_fisica = promedio_nota_fisica * 0.20
porcentaje_examen_fisica = examen_fisica * 0.80
nota_final_fisica = porcentaje_examen_fisica + porcentaje_nota_fisica
	
promedio_nota_quimica = (nota_1_quimica + nota_2_quimica + nota_3_quimica) / 3
porcentaje_nota_quimica = promedio_nota_quimica * 0.15
porcentaje_examen_quimica = examen_quimica * 0.85
nota_final_quimica = porcentaje_examen_quimica + porcentaje_nota_quimica
	
promedio_general_3_materias = (nota_final_fisica + nota_final_matematicas + nota_final_quimica) / 3
	
#salidas

print("Su nota final de matemáticas es de: ",nota_final_matematicas)
print("Su nota final de física es de: ",nota_final_fisica)
print("Su nota final de matemáticas es de: ",nota_final_quimica)
print("El promedio de las 3 materias es de: ",promedio_general_3_materias)