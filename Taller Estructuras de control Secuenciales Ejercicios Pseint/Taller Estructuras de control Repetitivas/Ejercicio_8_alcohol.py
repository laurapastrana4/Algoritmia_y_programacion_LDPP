#Ejercicio_8_alcohol
total_encuestados =0
encuestados_alcoholicos = 0
mujeres_menores = 0
hombre_sin_aguardiente = 0
edad_cerveza = 0
contador_cerveza = 0
total_whisky = 0 

while True:
    total_encuestados = total_encuestados + 1
    licor = input("¿Consume licor? (si/no): ")
    if licor == "si":
        encuestados_alcoholicos = encuestados_alcoholicos + 1
        
        licor_pref = int(input("¿Cuál es su licor preferido?: (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
        edad = int(input("¿Cuál es su edad?: "))
        sexo = input("¿Cuál es su sexo? (f/m): ")
        
        if sexo == "f" and edad < 18:
            mujeres_menores = mujeres_menores + 1
            
        if sexo == "m" and licor_pref != 1 and 20 <= edad <= 25:
            hombre_sin_aguardiente = hombre_sin_aguardiente + 1
            
        if licor_pref == 3:
            edad_cerveza = edad_cerveza + edad
            contador_cerveza = contador_cerveza + 1
        
        if licor_pref == 5:
            total_whisky = total_whisky + 1
    
    continuar = input("¿Desea continuar con la encuesta? (si/no): ")
    if continuar == "no":
        break
    
promedio_edad_cerveza = edad_cerveza / contador_cerveza
porcentaje_whisky = total_whisky / total_encuestados

print(f"Total de personas que consumen licor: {encuestados_alcoholicos}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {hombre_sin_aguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza}")
print(f"Porcentaje de personas que consumen whisky con respecto al total de personas encuestadas: {porcentaje_whisky}%")

