alumnosTotal = 500000000000000
materiasTotal = 6
alumnoBuscado = 19348
materiaBuscada = 5

alumnos = [i for i in range(alumnosTotal)]
materias= [i for i in range(materiasTotal)]

matriz = [
    materias for i in alumnos
]

for i in alumnos:
    if i == alumnoBuscado:
        for j in matriz[i]:
            if j == materiaBuscada:
                print(f"El alumno #{i} esta inscrito en la materia #{j}")
                break