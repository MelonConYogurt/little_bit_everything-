from datetime import datetime

# Lista de estudiantes
estudiantes = [
    {'nombre': 'Ana', 'fecha_nacimiento': '2000-05-15', 'calificaciones': [9.5, 8.7, 10.0]},
    {'nombre': 'Luis', 'fecha_nacimiento': '1998-11-22', 'calificaciones': [7.5, 6.0, 8.0]},
    {'nombre': 'Pedro', 'fecha_nacimiento': '2001-02-01', 'calificaciones': [10.0, 9.0, 8.5]},
    {'nombre': 'Laura', 'fecha_nacimiento': '2000-12-30', 'calificaciones': [6.5, 7.0, 8.0]},
]

def calcular_promedio(calificaciones:list)-> float:
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def promedio_calificaciones(estudiantes: list)-> list:
    return list(map(lambda estudiante: (estudiante['nombre'], estudiante['calificaciones'], calcular_promedio(estudiante['calificaciones'])), estudiantes))

def mejores_estudiantes(estudiantes: list)-> list:
    return list(filter(lambda estudiante: calcular_promedio(estudiante['calificaciones']) >= 9, estudiantes))

if __name__ == "__main__":
    print("Promedio de calificaciones:", promedio_calificaciones(estudiantes))
    print("Mejores estudaintes:", mejores_estudiantes(estudiantes))