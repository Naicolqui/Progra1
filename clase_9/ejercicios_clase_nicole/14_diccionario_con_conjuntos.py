# EJERCICIO 14 - Diccionario con conjuntos
#
# Dado el siguiente diccionario:

# Mostrar:
# 1. Los lenguajes o tecnologías que conoce Ana.
# 2. Los conocimientos que tienen en común Ana y Pedro.
# 3. Todos los conocimientos distintos presentes entre todos los estudiantes.

# Escribí tu solución debajo de esta línea:

def main(): 
    estudiantes = {
        "Ana": {"Python", "SQL", "HTML"},
        "Luis": {"Python", "Java"},
        "Marta": {"SQL", "HTML"},
        "Pedro": {"Python", "SQL"}
    }

    conocimientos_ana = estudiantes["Ana"]
    conocimientos_comunes = estudiantes["Ana"].intersection(estudiantes["Pedro"])
    todos_conocimientos = set().union(*estudiantes.values())

    print("Conocimientos de Ana:", conocimientos_ana)
    print("Conocimientos en común entre Ana y Pedro:", conocimientos_comunes)
    print("Todos los conocimientos distintos entre todos los estudiantes:", todos_conocimientos)

if __name__ == "__main__":
    main()