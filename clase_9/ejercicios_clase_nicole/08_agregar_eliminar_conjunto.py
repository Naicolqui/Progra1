# EJERCICIO 8 - Agregar y eliminar elementos de un conjunto
#
# Dado el siguiente conjunto:

# 1. Agregar "Ingles".
# 2. Eliminar "Fisica".
# 3. Mostrar el conjunto resultante.

# Escribí tu solución debajo de esta línea:

def main():
    materias = {"Programacion", "Matematica", "Fisica"}

    materias.add("Ingles")
    materias.remove("Fisica")

    print(materias)

if __name__ == "__main__":
    main()