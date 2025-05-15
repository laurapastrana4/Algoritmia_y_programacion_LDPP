positivos=0
suma=0

for i in range(6):
    a=float(input())
    if a >0:
        positivos=positivos+1
        suma=suma+a

promedio=suma/positivos
print(f"{positivos} valores positivos")
print(f"{promedio}")