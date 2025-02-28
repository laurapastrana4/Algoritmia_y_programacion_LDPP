#Ejercicio_10_categoria_trabajador
#Entradas
categoria = int(input("Ingrese la categoría del trabajador (1-5): "))

#caja negra
sueldo_cat_1 = 5000000
sueldo_cat_2 = 4300000
sueldo_cat_3 = 3600000
sueldo_cat_4 = 2000000
sueldo_cat_5 = 900000

if categoria == 1:
    aumento = 0.10 + sueldo_cat_1
elif categoria == 2:
    aumento = 0.15 + sueldo_cat_2
elif categoria == 3:
    aumento = 0.20 + sueldo_cat_3
elif categoria == 4:
    aumento = 0.40 + sueldo_cat_4
elif categoria == 5:
    aumento = 0.60 + sueldo_cat_5
else:
    print("La categoría ingresada no es válida. Ingrese un valor entre 1 y 5.")
    
#saldidas
print(f"El nuevo sueldo bruto del trabajador es: {aumento} COP")
print(f"La categoría del trabajador es: {categoria}")
