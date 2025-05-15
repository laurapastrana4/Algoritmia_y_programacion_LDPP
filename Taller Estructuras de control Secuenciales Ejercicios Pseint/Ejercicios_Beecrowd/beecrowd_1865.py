casos=int(input())
for i in range(casos):
    entrada=input().split()
    nombre=entrada[0]
    fuerza=int(entrada[1])
    if nombre =="Thor":
        print ("Y")
    else:
        print ("N")