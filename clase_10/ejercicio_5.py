
def cargar_productos():
    with open("productos.csv", "wt", encoding="utf-8") as archivo:
        archivo.write("codigo;descripcion;cantidad;precio\n")

        while True:
            codigo = input("Código del producto (FIN para terminar): ").strip()

            if codigo.upper() == "FIN":
                break

            descripcion = input("Descripción: ").strip()

            while True:
                try:
                    cantidad = int(input("Cantidad: "))
                    if cantidad >= 0:
                        break
                    print("La cantidad debe ser mayor o igual a cero.")
                except ValueError:
                    print("Ingresá una cantidad entera válida.")

            while True:
                try:
                    precio = float(input("Precio: ").replace(",", "."))
                    if precio > 0:
                        break
                    print("El precio debe ser mayor que cero.")
                except ValueError:
                    print("Ingresá un precio válido.")

            archivo.write(
                f"{codigo};{descripcion};{cantidad};{precio}\n"
            )


def leer_productos():
    productos = []

    with open("productos.csv", "rt", encoding="utf-8") as archivo:
        encabezado = archivo.readline()

        for linea in archivo:
            campos = linea.strip().split(";")

            if len(campos) != 4:
                print("Registro inválido: cantidad incorrecta de campos.")
                continue

            codigo, descripcion, cantidad, precio = campos

            try:
                cantidad = int(cantidad)
                precio = float(precio)

                if cantidad < 0 or precio <= 0:
                    print("Registro inválido: cantidad o precio incorrecto.")
                    continue

                productos.append(
                    (codigo, descripcion, cantidad, precio)
                )

            except ValueError:
                print("Registro inválido: datos numéricos incorrectos.")

    return productos


def informar_importes(productos):
    total = 0

    print("\n--- IMPORTES POR PRODUCTO ---")

    for codigo, descripcion, cantidad, precio in productos:
        importe = cantidad * precio
        total += importe

        print(f"{codigo} - {descripcion}: ${importe:.2f}")

    print(f"\nImporte total: ${total:.2f}")


def informar_stock_bajo(productos):
    print("\n--- PRODUCTOS CON CANTIDAD MENOR A 5 ---")

    encontrados = False

    for codigo, descripcion, cantidad, precio in productos:
        if cantidad < 5:
            print(f"{codigo} - {descripcion}: {cantidad} unidades")
            encontrados = True

    if not encontrados:
        print("No hay productos con cantidad menor a 5.")


def main():
    cargar_productos()

    productos = leer_productos()

    informar_importes(productos)

    informar_stock_bajo(productos)


main()
