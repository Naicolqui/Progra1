# EJERCICIO 7 - Crear y recorrer un conjunto
#
# Dada la siguiente lista con elementos repetidos:

# Crear un conjunto con los lenguajes sin repetir.
# Luego recorrerlo y mostrar cada lenguaje.

# Escribí tu solución debajo de esta línea:

def main():
    lenguajes = ["Python", "Java", "Python", "C", "Java", "C++"]

    conjunto_lenguajes = set(lenguajes)

    for lenguaje in conjunto_lenguajes:
        print(lenguaje)

if __name__ == "__main__":
    main()