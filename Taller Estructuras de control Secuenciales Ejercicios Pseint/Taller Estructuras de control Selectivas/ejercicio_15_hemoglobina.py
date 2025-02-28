#ejercicio_15_hemoglobina
#entradas
edad=int(input("Ingrese la edad: "))
h=float(input("Ingrese nivel de hemoglobina: "))
sexo=input("Ingrese su sexo (F=Femenino, M=Masculino): ")
anemia=""
#Caja negra
if(edad>0 and edad<=1 and h<13 and h>=26):
    anemia="positivo"
elif(edad>1 and edad<=6 and h<10 and h>=18):
    anemia="positivo" 
elif(edad>6 and edad<=10 and h<11 and h>=15):
    anemia="positivo"   
elif(edad>10 and edad<=15 and h<13 and h>=15.5):
    anemia="positivo" 
elif(sexo == 'F' and edad>15 and h<12 and h>=16):
    anemia="positivo" 
elif(sexo == 'M' and edad>15 and h<14 and h>=18):
    anemia="positivo" 
else:
    anemia="negativo"
    
print("Segun el test el resultado es: ",anemia)