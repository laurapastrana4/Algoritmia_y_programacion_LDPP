estudiantes = {
    "1": {"nombre": "Lorea", "nota": 8},
    "2": {"nombre": "Markel", "nota": 4.2},
    "3": {"nombre": "Julen", "nota": 6.5}
}

contador = 4

while contador <= 10:
    nombre=input("Ingrese nombre: ")
    nota=float(input("Ingrese nota: "))
    estudiantes[contador] = {"nombre": nombre, "nota": nota}
    contador = contador+1

aprobados = []
suspendidos = []
suma_notas = 0

for i in estudiantes.values():
    nota = i["nota"]
    suma_notas = suma_notas+nota
    if nota >= 5:
        aprobados.append(i["nombre"])
    else:
        suspendidos.append(i["nombre"])

promedio = suma_notas / len(estudiantes)

print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes suspendidos: {suspendidos}")
print(f"Nota media de la clase: {promedio}")