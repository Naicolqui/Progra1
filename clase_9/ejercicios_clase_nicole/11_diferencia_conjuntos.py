# EJERCICIO 11 - Diferencia de conjuntos
#
# Dados los siguientes conjuntos:

# Mostrar los alumnos que están inscriptos pero no asistieron.

# Escribí tu solución debajo de esta línea:

def main():
    inscriptos = {"Ana", "Luis", "Marta", "Pedro", "Sofia"}
    presentes = {"Ana", "Marta", "Sofia"}

    alumnos_no_asistieron = inscriptos.difference(presentes)

    print("Alumnos inscriptos que no asistieron:", alumnos_no_asistieron)

if __name__ == "__main__":
    main()