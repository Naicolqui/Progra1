# EJERCICIO 2 - Agregar y modificar elementos
#
# Dado el siguiente diccionario de producto:

# 1. Agregar la clave "marca" con el valor "Logitech".
# 2. Cambiar el precio a 28000.
# 3. Mostrar el diccionario completo.

# Escribí tu solución debajo de esta línea:

def main():
    producto = {
        "nombre": "Teclado",
        "precio": 25000,
        "stock": 10
    }

    producto["marca"] = "Logitech"
    producto["precio"] = 28000

    print(producto)

if __name__ == "__main__":
    main()