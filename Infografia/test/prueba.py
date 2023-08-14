estudiantes = [
    {
        "nombre completo":" juan perez",
        "edad":16,
        "notas":{
            "Mat":70,
            "fis":80,
            "qmc":90,
            "lab":60
        },
        "asistencia ":85
    },
     {
        "nombre completo":" rosa perez",
        "edad":17,
        "notas":{
            "Mat":40,
            "fis":50,
            "qmc":60,
            "lab":100,
        },
        "asistencia ":100
    }
]

def promedio_estudiante(estudiante: dict) -> float:
    total_notas = 0
    total_materias = 0

    # Iteramos sobre las notas del estudiante y calculamos el total de notas y materias
    for nota in estudiante["notas"].values():
        total_notas += nota
        total_materias += 1

    # Calculamos el promedio del estudiante
    promedio = total_notas / total_materias
    return promedio

def promedio_curso(lista_estudiante: list) -> float:
    total_notas = 0
    total_materias = 0

    # Iteramos sobre todos los estudiantes en la lista
    for estudiante in lista_estudiante:
        # Iteramos sobre las notas del estudiante y sumamos el total de notas y materias
        for nota in estudiante["notas"].values():
            total_notas += nota
            total_materias += 1

    # Calculamos el promedio del curso
    promedio = total_notas / total_materias
    return promedio

# Calcular promedio para cada estudiante e imprimir
for estudiante in estudiantes:
    nombre = estudiante["nombre completo"]
    promedio_est = promedio_estudiante(estudiante)
    print(f"Promedio de {nombre}: {promedio_est}")

# Calcular promedio del curso e imprimir
promedio_curso_total = promedio_curso(estudiantes)
print(f"Promedio del curso: {promedio_curso_total}")