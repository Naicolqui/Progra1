# Ejercicio 5 - Archivos CSV y encabezados


ARCHIVO = "productos.csv"
ENCABEZADO = "codigo;descripcion;cantidad;precio"


def cargar_productos():
    try:
       
        archivo = open(ARCHIVO, "wt", encoding="utf-8")
    except OSError as error:
        print("No se pudo crear el archivo:", error)
    else:
        archivo.write(ENCABEZADO + "\n")

        while True:
            codigo = input("Código del producto (FIN para terminar): ").strip()

            if codigo.upper() == "FIN":    
                break

            if codigo == "" or ";" in codigo:
                print("El código no puede estar vacío ni contener ';'.")
                continue

            descripcion = input("Descripción: ").strip()
            while descripcion == "" or ";" in descripcion:
                print("La descripción no puede estar vacía ni contener ';'.")
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

            archivo.write(f"{codigo};{descripcion};{cantidad};{precio}\n")

        
        archivo.close()


def leer_productos():
    productos = []

    try:
        archivo = open(ARCHIVO, "rt", encoding="utf-8")
    except OSError as error:
        print("No se pudo abrir el archivo:", error)
    else:
        
        encabezado = archivo.readline().rstrip("\n")
        if encabezado != ENCABEZADO:
            print("Atención: el archivo no tiene el encabezado esperado.")

        for linea in archivo:
            campos = linea.rstrip("\n").split(";")

            if len(campos) != 4:
                print("Registro inválido: cantidad incorrecta de campos.")
                continue

            codigo, descripcion, cantidad, precio = campos

            if codigo.strip() == "" or descripcion.strip() == "":
                print("Registro inválido: código o descripción vacíos.")
                continue

            try:
                cantidad = int(cantidad)
                precio = float(precio)
            except ValueError:
                print("Registro inválido: datos numéricos incorrectos.")
                continue

            if cantidad < 0 or precio <= 0:
                print("Registro inválido: cantidad o precio incorrecto.")
                continue

            productos.append((codigo, descripcion, cantidad, precio))

    
        archivo.close()

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

    if len(productos) == 0:
        print("No hay productos válidos para informar.")
    else:
        informar_importes(productos)
        informar_stock_bajo(productos)


main()
