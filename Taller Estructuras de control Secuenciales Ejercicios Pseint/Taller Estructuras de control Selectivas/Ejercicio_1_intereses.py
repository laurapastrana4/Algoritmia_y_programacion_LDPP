#Ejercicio_1_intereses
# Entradas
inversion = float(input("Ingrese la cantidad de dinero en inversión: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en %): "))

# Caja negra
intereses = inversion * (tasa_interes / 100)

if intereses > 100000:
    total_final = inversion + intereses
    print(f"Los intereses generados son: {intereses} COP")
    print(f"Dado que los intereses exceden $100,000 COP, se reinvertirán.")
    print(f"El monto final en la cuenta será: {total_final} COP")
else:
    total_final = inversion
    print(f"Los intereses generados son: {intereses} COP")
    print(f"Dado que los intereses no exceden $100,000 COP, no se reinvertirán.")
    print(f"El monto final en la cuenta será: {total_final} COP")