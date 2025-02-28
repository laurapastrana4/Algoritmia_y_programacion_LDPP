#Ejercicio_16_ecuacion
#entradas
import math
n=input()
(A,B,C)=n.split(" ")
A=int(A)
B=int(B)
C=int(C)

D = B**2-4*A*C

if D == 0:
    X1 = X2 = -B / (2*A)
    print (X1)
elif D > 0:
    X1 = (-B + math.sqrt(D)) / (2*A)
    X2 = (-B - math.sqrt(D)) / (2*A)
    print (x1), (x2)
    
else:
    print("La ecuación no tiene solución en los números reales.")