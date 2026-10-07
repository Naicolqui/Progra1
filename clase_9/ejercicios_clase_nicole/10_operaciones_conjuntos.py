# EJERCICIO 10 - Unión e intersección
#
# Dados los siguientes conjuntos:

# Mostrar:
# 1. Todos los alumnos que cursan al menos uno de los dos lenguajes.
# 2. Los alumnos que cursan ambos lenguajes.

# Escribí tu solución debajo de esta línea:

def main():
    python = {"Ana", "Luis", "Marta", "Juan"}
    java = {"Pedro", "Luis", "Juan", "Sofia"}

    alumnos_union = python.union(java)
    alumnos_interseccion = python.intersection(java)

    print("Alumnos que cursan al menos uno de los dos lenguajes:", alumnos_union)
    print("Alumnos que cursan ambos lenguajes:", alumnos_interseccion)

if __name__ == "__main__":
    main()