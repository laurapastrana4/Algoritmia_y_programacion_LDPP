#Ejercicio_6_redondear
# Entradas
n=input()
(a,b,c,d)=n.split(" ")
a=int(a)
b=int(b)
c=int(c)
d=int(d)

# Cajaa negra
N = a * 1000 + b * 100 + c * 10 + d
ultima_centena=(c,d)
if ultima_centena < 50:
    resultado = N - ultima_centena
elif ultima_centena >= 50:
    resultado = N + (100 - ultima_centena)
# Salidas
print(f"El número {n} redondeado a la centena más cercana es: {resultado}")
