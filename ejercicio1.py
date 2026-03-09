def validar_estudiante(estudiante):
    if len(estudiante["materias"]) < 3:
        print(" Debe tener al menos 3 materias.")
        return False
    for materia, nota in estudiante["notas"].items():
        if nota < 0.0 or nota > 5.0:
            print(f" La nota de {materia} debe estar entre 0.0 y 5.0.")
            return False
    return True

def calcular_reporte(estudiante):
    notas = estudiante["notas"]
    promedio = sum(notas.values()) / len(notas)
    mejor = max(notas, key=notas.get)
    peor = min(notas, key=notas.get)
    return promedio, mejor, peor

def mostrar_reporte(estudiante):
    print(f"\n--- {estudiante['nombre']} ---")
    print(f"Edad   : {estudiante['edad']} años")
    print(f"Estado : {'Activo' if estudiante['activo'] else 'Inactivo'}")
    print(f"Materias: {', '.join(estudiante['materias'])}")

    if not validar_estudiante(estudiante):
        return

    promedio, mejor, peor = calcular_reporte(estudiante)

    print(f"Promedio: {promedio:.2f}")
    print(f"Mejor nota : {mejor} ({estudiante['notas'][mejor]})")
    print(f"Peor nota  : {peor} ({estudiante['notas'][peor]})")
    print(f"Resultado  : {'APRUEBA ' if promedio >= 3.0 else 'REPRUEBA '}")

def main():
    estudiantes = [
        {
            "nombre": "Sainner",
            "edad": 20,
            "activo": True,
            "materias": ["Estructura de Datos", "Física", "Programación"],
            "notas": {"Estructura de Datos": 4.5, "Física": 3.2, "Programación": 2.8}
        },
        {
            "nombre": "Elkin",
            "edad": 19,
            "activo": True,
            "materias": ["Base de Datos", "Análisis de Sistemas", "Arquitectura del Computador"],
            "notas": {"Base de Datos": 2.5, "Análisis de Sistemas": 2.8, "Arquitectura del Computador": 3.9}
        },
        {
            "nombre": "Ana",                         
            "edad": 19,
            "activo": False,
            "materias": ["Inglés", "Arte"],
            "notas": {"Inglés": 4.0, "Arte": 4.0}   
        }
    ]

    for estudiante in estudiantes:
        mostrar_reporte(estudiante)

if __name__ == "__main__":
    main()