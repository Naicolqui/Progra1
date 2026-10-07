# EJERCICIO 12 - Diccionario y conjunto
#
# Dado el siguiente diccionario:

# Y el siguiente conjunto de DNI presentes:

# Mostrar el nombre de los alumnos presentes.

# Escribí tu solución debajo de esta línea:

def main():
    alumnos = {
        1001: "Ana",
        1002: "Luis",
        1003: "Marta",
        1004: "Pedro"
    }
    presentes = {1001, 1003}

    for dni in presentes:
        if dni in alumnos:
            print(alumnos[dni])

if __name__ == "__main__":
    main()