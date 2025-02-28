#Ejercicio_8_PyQ
#Entradas
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))

#Caja negra
resultado = P**3 + Q**4 - 2*P**2

if resultado > 680:
    print(f'Los valores P = {P} y Q = {Q} satisfacen la expresión')
else:
    print(f'Los valores P = {P} y Q = {Q} no satisfacen la expresión')