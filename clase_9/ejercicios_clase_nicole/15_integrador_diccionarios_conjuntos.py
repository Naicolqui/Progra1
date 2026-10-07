# EJERCICIO 15 - Integrador de diccionarios y conjuntos
#
# Se dispone del siguiente diccionario.
# Cada clave es el nombre de un alumno y el valor es un conjunto
# con las materias que aprobó.


# Resolver:
#
# 1. Mostrar todas las materias diferentes que aparecen.
# 2. Mostrar qué alumnos aprobaron "Programacion".
# 3. Mostrar qué materias aprobaron tanto Ana como Sofia.
# 4. Mostrar qué materias aprobó Ana pero no Luis.
# 5. Crear un diccionario nuevo donde la clave sea una materia y
#    el valor sea la cantidad de alumnos que la aprobaron.
#
# Ejemplo parcial del punto 5:
# {
#     "Programacion": 4,
#     "Matematica": 4,
#     ...
# }
#

# Escribí tu solución debajo de esta línea:

def main():
    aprobadas = {
        "Ana": {"Programacion", "Matematica", "Ingles"},
        "Luis": {"Programacion", "Ingles"},
        "Marta": {"Programacion", "Matematica", "Fisica"},
        "Pedro": {"Matematica", "Fisica"},
        "Sofia": {"Programacion", "Matematica", "Ingles", "Fisica"}
    }

    # 1. Mostrar todas las materias diferentes que aparecen.
    todas_materias = set().union(*aprobadas.values())
    print("Todas las materias diferentes:", todas_materias)

    # 2. Mostrar qué alumnos aprobaron "Programacion".
    alumnos_programacion = [alumno for alumno, materias in aprobadas.items() if "Programacion" in materias]
    print("Alumnos que aprobaron Programacion:", alumnos_programacion)

    # 3. Mostrar qué materias aprobaron tanto Ana como Sofia.
    materias_ana_sofia = aprobadas["Ana"].intersection(aprobadas["Sofia"])
    print("Materias aprobadas tanto por Ana como por Sofia:", materias_ana_sofia)

    # 4. Mostrar qué materias aprobó Ana pero no Luis.
    materias_ana_no_luis = aprobadas["Ana"].difference(aprobadas["Luis"])
    print("Materias que aprobó Ana pero no Luis:", materias_ana_no_luis)

    # 5. Crear un diccionario nuevo donde la clave sea una materia y el valor sea la cantidad de alumnos que la aprobaron.
    conteo_materias = {}
    for materia in todas_materias:
        conteo_materias[materia] = sum(1 for materias in aprobadas.values() if materia in materias)
    
    print("Cantidad de alumnos que aprobaron cada materia:", conteo_materias)

if __name__ == "__main__":
    main()