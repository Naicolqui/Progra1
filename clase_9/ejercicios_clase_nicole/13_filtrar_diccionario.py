# EJERCICIO 13 - Filtrar datos de un diccionario
#
# Dado el siguiente diccionario:

# Crear un nuevo diccionario solamente con los productos
# cuyo precio sea mayor a 30000.
#
# Escribí tu solución debajo de esta línea:

def main():
    productos = {
        "mouse": 15000,
        "teclado": 30000,
        "monitor": 200000,
        "parlantes": 25000,
        "notebook": 850000
    }

    productos_filtrados = {producto: precio for producto, precio in productos.items() if precio > 30000}
    print(productos_filtrados)

if __name__ == "__main__":
    main()