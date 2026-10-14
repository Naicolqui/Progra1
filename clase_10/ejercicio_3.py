""" 3. Escritura de registros de texto
Desarrollar una función crear_alumnos() que genere alumnos.txt. Por cada alumno se ingresarán legajo, nombre y
apellido, y comisión. La carga finalizará con un legajo igual a -1; ese valor de corte no debe grabarse.
Cada registro deberá almacenarse en una línea con sus campos separados por punto y coma. Antes de escribir, validen
que el legajo sea positivo, que el nombre no esté vacío y que la comisión tenga un formato válido (valor numérico de 1 a 10).
Prueben la función con varios alumnos. Luego ejecútenla nuevamente usando modo "wt" y expliquen qué ocurrió con los
datos anteriores. Repitan con modo "at" y comparen los resultados. """


def crear_alumnos(modo="wt"):
    try:
        arch = open("alumnos.txt", modo, encoding="utf-8")
    except OSError as error:
        print("No se pudo crear el archivo:", error)
        return

    try:
        while True:
            try:
                legajo = int(input("Ingrese un legajo (-1 para finalizar): "))
            except ValueError:
                print("El legajo debe ser un número entero.")
                continue

            if legajo == -1:
                break

            if legajo <= 0:
                print("El legajo debe ser positivo.")
                continue

            nombre = input("Ingrese nombre y apellido: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue

            try:
                comision = int(input("Ingrese comisión (1 a 10): "))
            except ValueError:
                print("La comisión debe ser un número entero.")
                continue

            if comision < 1 or comision > 10:
                print("La comisión debe estar entre 1 y 10.")
                continue

            arch.write(str(legajo) + ";" + nombre + ";" + str(comision) + "\n")
    finally:
        arch.close()


def main():
    crear_alumnos("wt")


main()
