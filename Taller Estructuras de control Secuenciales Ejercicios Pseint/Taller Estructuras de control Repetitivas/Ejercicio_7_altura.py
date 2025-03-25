#Ejercicio_7
max_altura = 0
estu = int(input("Ingrese cantidad de estudiantes: "))
for a in range (estu):
    altura = float(input("Ingrese la altura: "))
    a = a+1
    if altura > max_altura:
        max_altura = altura
print (f"La altura maxima es : {max_altura}")