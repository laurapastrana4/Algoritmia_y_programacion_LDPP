#Entradas
lado_a = int(input("Ingrese la longitud del lado A"))
lado_b = int(input("Ingrese la longitud del lado B"))
lado_c = int(input("Ingrese la longitud del lado C"))

#caja negra
import math
S = (lado_a + lado_c + lado_c) / 2
area = math.sqrt(S * ( S - lado_a) * (S - lado_b) *( S - lado_c))

#salidas
print("El área del triangulo es: ",area)
