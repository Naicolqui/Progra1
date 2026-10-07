# EJERCICIO 5 - Contar apariciones
#
# Dada la siguiente lista:

# Crear un diccionario que indique cuántas veces aparece cada color.
#
# Resultado esperado:
# {'rojo': 3, 'azul': 2, 'verde': 1}

# Escribí tu solución debajo de esta línea:

def main():
    colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]

    contador_colores = {}

    for color in colores:
        if color in contador_colores:
            contador_colores[color] += 1
        else:
            contador_colores[color] = 1

    print(contador_colores)

if __name__ == "__main__":
    main()