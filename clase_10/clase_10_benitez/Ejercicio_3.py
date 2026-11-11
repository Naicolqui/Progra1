def crear_alumnos(modo="wt"):
    try:
        with open("alumnos.txt", modo, encoding="utf-8") as arch:
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
                if nombre == "" or ";" in nombre:
                    print("El nombre no puede estar vacío ni contener ';'.")
                    continue

                try:
                    comision = int(input("Ingrese comisión (1 a 10): "))
                except ValueError:
                    print("La comisión debe ser un número entero.")
                    continue

                if comision < 1 or comision > 10:
                    print("La comisión debe estar entre 1 y 10.")
                    continue

                arch.write(f"{legajo};{nombre};{comision}\n")
    except OSError as error:
        print("No se pudo crear el archivo:", error)
    finally:
        print("Se completo la carga del archivo")


def main():
    crear_alumnos("wt")


if __name__ == "__main__":
    main()