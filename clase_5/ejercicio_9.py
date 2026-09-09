"""9. Desafío integrador: carga segura de productos 
Desarrollen un sistema modular que registre productos en una lista. Cada producto podrá almacenarse como una lista con 
código, descripción, cantidad y precio. La carga finaliza cuando el código ingresado sea "FIN". 
El programa deberá: 
• Utilizar while True y break para finalizar la carga. 
• Capturar ValueError al convertir cantidad y precio. 
• Utilizar raise ValueError para rechazar cantidades o precios menores o iguales a cero. 
• No incorporar un producto cuando sus datos sean inválidos. 
• Calcular el importe de cada producto mediante una función. 
• Utilizar assert para comprobar una condición interna del cálculo, no para validar la entrada. 
• Informar cantidad de productos, importe total y precio promedio; si no se cargaron productos, evitar la división por 
cero."""

def calcular_importe(cantidad, precio):
    assert cantidad > 0 and precio > 0, "Error interno: cantidad y precio deben ser positivos para calcular importe."
    return cantidad * precio


def cargar_productos():
    lista_productos = []

    while True:
        codigo = input("Ingrese el código del producto (o 'FIN' para finalizar): ")
        if codigo.upper() == "FIN":
            break

        descripcion = input("Ingrese la descripción del producto: ")

        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero.")

            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a cero.")

        except ValueError as e:
            print(f"❌ Error al ingresar los datos: {e}. El producto no fue ingresado.\n")
            continue

        producto = [codigo, descripcion, cantidad, precio]
        lista_productos.append(producto)
        print("✅ Producto registrado correctamente.\n")

    return lista_productos


def main():
    productos = cargar_productos()

    cant_productos = len(productos)
    print(f"\n--- RESUMEN DE CARGA ---")
    print(f"Cantidad de productos ingresados: {cant_productos}")

    if cant_productos > 0:
        importe_total = 0
        suma_precios = 0

        for prod in productos:
            cant = prod[2]
            precio = prod[3]
            importe_total += calcular_importe(cant, precio)
            suma_precios += precio

        precio_promedio = suma_precios / cant_productos

        print(f"Importe total acumulado: ${importe_total:.2f}")
        print(f"Precio promedio por producto: ${precio_promedio:.2f}")
    else:
        print("No se cargaron productos. Se evita la división por cero.")


if __name__ == "__main__":
    main()