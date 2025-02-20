# Entradas
print ("Su calificación final de Cómputo se compone por: ")
print ("55% de promedio de parciales, 30% de examen final y 15% de trabajo final")

nota1 = float(input("Ingrese su nota 1:"))
nota2 = float(input("Ingrese su nota 2:"))
nota3 = float(input("Ingrese su nota 3:"))
examen_final = float(input("Ingrese su calificación del examen final: "))
trabajo_final = float(input("Ingrese su calificación del trabajo final: "))

#caja negra
promedio_notas=(nota1+nota2+nota3)/3
porcentaje_notas=promedio_notas*0.55
porcentaje_examen=examen_final*0.30
porcentaje_trabajo=trabajo_final*0.15
calificación_final=porcentaje_examen+porcentaje_notas+porcentaje_trabajo

#salidas
print("Su calificación final de Cómputo es de: ",calificación_final)