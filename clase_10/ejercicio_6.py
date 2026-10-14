""" 6. Manejo de excepciones
Revisen los ejercicios anteriores para manejar errores sin utilizar except: de manera indiscriminada. Contemplen, como
mínimo:
a) OSError al abrir, crear o escribir un archivo.
b) ValueError al convertir legajos, cantidades, precios o porcentajes.
c) Registros incompletos o con una cantidad inesperada de campos.
Comparen try-except-finally con with. Si se utiliza finally, la variable del archivo debe inicializarse y verificarse antes de
cerrarla, porque la apertura podría fallar. Para la mayoría de estos ejercicios, with es la alternativa más clara y segura. """


def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Debe ingresar un número entero.")
        return None


def crear_alumnos():
    try:
        with open("alumnos.txt", "wt", encoding="utf-8") as arch:
            while True:
                legajo = leer_entero("Ingrese un legajo (-1 para finalizar): ")
                if legajo is None:
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

                comision = leer_entero("Ingrese comisión (1 a 10): ")
                if comision is None:
                    continue
                if comision < 1 or comision > 10:
                    print("La comisión debe estar entre 1 y 10.")
                    continue

                arch.write(f"{legajo};{nombre};{comision}\n")
    except OSError as error:
        print("No se pudo acceder al archivo:", error)


def mostrar_alumnos():
    por_comision = {}
    invalidas = []

    try:
        with open("alumnos.txt", "rt", encoding="utf-8") as arch:
            print("\n--- ALUMNOS VÁLIDOS ---")
            for numero, linea in enumerate(arch, 1):
                campos = linea.rstrip("\n").split(";")

                if len(campos) != 3:
                    invalidas.append((numero, linea.rstrip("\n")))
                    continue

                legajo, nombre, comision = campos

                try:
                    legajo = int(legajo)
                    int(comision)
                except ValueError:
                    invalidas.append((numero, linea.rstrip("\n")))
                    continue

                print(f"{legajo} - {nombre} - comisión {comision}")
                if legajo > 10000:
                    print("   (legajo mayor a 10000)")
                por_comision[comision] = por_comision.get(comision, 0) + 1
    except OSError as error:
        print("No se pudo leer el archivo:", error)
        return

    print("\n--- ALUMNOS POR COMISIÓN ---")
    for comision in sorted(por_comision, key=int):
        print("Comisión", comision, ":", por_comision[comision])

    if invalidas:
        print("\n--- LÍNEAS CON FORMATO INVÁLIDO ---")
        for numero, linea in invalidas:
            print("Línea", numero, ":", linea)


def informar_productos():
    total = 0
    try:
        with open("productos.csv", "rt", encoding="utf-8") as arch:
            arch.readline() 
            for linea in arch:
                campos = linea.rstrip("\n").split(";")
                if len(campos) != 4:
                    print("Registro omitido (cantidad de campos incorrecta):", linea.rstrip("\n"))
                    continue

                codigo, descripcion, cantidad, precio = campos
                try:
                    cantidad = int(cantidad)
                    precio = float(precio)
                except ValueError:
                    print("Registro omitido (datos numéricos inválidos):", linea.rstrip("\n"))
                    continue

                if cantidad < 0 or precio <= 0:
                    print("Registro omitido (cantidad o precio fuera de rango):", linea.rstrip("\n"))
                    continue

                importe = cantidad * precio
                total += importe
                print(f"{codigo} - {descripcion}: ${importe:.2f}")
                if cantidad < 5:
                    print("   Stock bajo:", cantidad, "unidades")
    except OSError as error:
        print("No se pudo acceder al archivo:", error)
        return

    print(f"Importe total: ${total:.2f}")


def main():
    crear_alumnos()
    mostrar_alumnos()
    informar_productos()


main()
