# EJERCICIO 6 - Diccionario con listas
#
# Dado el siguiente diccionario:

# 1. Agregar "Marta" al curso de Programacion.
# 2. Mostrar todos los alumnos de Matematica.
# 3. Mostrar cuántos alumnos tiene cada curso.

# Escribí tu solución debajo de esta línea:

def main():
    cursos = {
        "Programacion": ["Ana", "Luis"],
        "Matematica": ["Pedro", "Sofia"],
        "Ingles": ["Juan"]
    }

    cursos["Programacion"].append("Marta")

    print("Alumnos de Matematica:", cursos["Matematica"])

    for curso, alumnos in cursos.items():
        print(f"{curso} tiene {len(alumnos)} alumnos.")

if __name__ == "__main__":
    main()