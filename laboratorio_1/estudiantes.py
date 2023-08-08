class Evaluador:
    def __init__(self, estudiantes, min_asistencia, max_extras):
        self.estudiantes = estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        resultados = []
        for estudiante in self.estudiantes:
            nombre_completo = f"{estudiante['nombre'].capitalize()} {estudiante['apellido'].capitalize()}"
            promedio_final = 0

            if 'notas' in estudiante and estudiante['notas']:
                total_notas = sum(estudiante['notas'].values())
                promedio_final = total_notas / len(estudiante['notas'])

            if estudiante['asistencia'] >= self.min_asistencia:
                promedio_final += sum(estudiante['extras'])
                promedio_final = min(promedio_final, 100)
                promedio_final = min(promedio_final, promedio_final + self.max_extras)

            resultados.append({'nombre_completo': nombre_completo, 'promedio': promedio_final})

        return resultados

    def obtener_mejor_estudiante(self):
        estudiantes_calculados = self.calcular_promedios()
        mejor_estudiante = max(estudiantes_calculados, key=lambda x: x['promedio'])
        return mejor_estudiante

    def salvar_datos(self, nombre_archivo):
        resultados = self.calcular_promedios()
        with open(nombre_archivo, 'w') as file:
            file.write('Nombre Completo,Asistencia,MAT,FIS,QMC,LAB,Total Extras,Promedio Final,Observación\n')
            for estudiante in resultados:
                promedio_final = estudiante['promedio']
                observacion = 'APROBADO' if promedio_final > 50 else 'REPROBADO'
                line = f"{estudiante['nombre_completo']},"

                if 'asistencia' in estudiante:
                    line += f"{estudiante['asistencia']},"
                else:
                    line += "0,"

                notas = estudiante.get('notas', {}) 
                line += f"{notas.get('MAT', 0)},{notas.get('FIS', 0)}"
                line += f",{notas.get('QMC', 0)},{notas.get('LAB', 0)}"

                extras = estudiante.get('extras', []) 
                line += f",{sum(extras)},{promedio_final},{observacion}\n"
                file.write(line)


estudiantes = [
    {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'notas': {
            'MAT': 87,
            'QMC': 76,
            'FIS': 56,
            'LAB': 78
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'María',
        'apellido': 'Gómez',
        'notas': {
            'MAT': 65,
            'QMC': 72,
            'FIS': 80,
            'LAB': 85
        },
        'extras': [1, 2, 3, 0, 2],
        'asistencia': 85
    },
    {
        'nombre': 'Pedro',
        'apellido': 'Lopez',
        'notas': {
            'MAT': 50,
            'QMC': 60,
            'FIS': 70,
            'LAB': 80
        },
        'extras': [0, 0, 1, 3, 1],
        'asistencia': 70
    },
    {
        'nombre': 'Ana',
        'apellido': 'Martinez',
        'notas': {},
        'extras': [2, 1, 1, 0, 0],
        'asistencia': 75
    }
]

evaluador = Evaluador(estudiantes, min_asistencia=70, max_extras=10)
resultados = evaluador.calcular_promedios()
mejor_estudiante = evaluador.obtener_mejor_estudiante()
evaluador.salvar_datos('resultado_notas.csv')

print("Resultados de los estudiantes:")
for estudiante in resultados:
    print(f"{estudiante['nombre_completo']}: {estudiante['promedio']}")

print("\nMejor estudiante:")
print(f"{mejor_estudiante['nombre_completo']}: {mejor_estudiante['promedio']}")
