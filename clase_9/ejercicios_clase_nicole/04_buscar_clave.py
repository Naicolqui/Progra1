# EJERCICIO 4 - Buscar una clave
#
# Dado el siguiente diccionario:

# Pedir al usuario que ingrese un país.
# Si el país existe en el diccionario, mostrar su capital.
# Si no existe, mostrar "País no encontrado".

# Escribí tu solución debajo de esta línea:


def main():
    capitales = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Uruguay": "Montevideo"
    }

    pais = input("Ingrese un país: ").capitalize().strip()

    if pais in capitales:
        print(f"La capital de {pais} es {capitales[pais]}.")
    else:
        print("País no encontrado.")

if __name__ == "__main__":
    main()