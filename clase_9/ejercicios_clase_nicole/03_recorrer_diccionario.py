# EJERCICIO 3 - Recorrer un diccionario
#
# Dado el siguiente diccionario:

# Mostrar cada alumno junto con su nota.
# Ejemplo:
# Ana obtuvo 8

# Escribí tu solución debajo de esta línea:

def main():
    notas = {
        "Ana": 8,
        "Luis": 6,
        "Marta": 9,
        "Pedro": 5
    }

    for alumno, nota in notas.items():
        print(f"{alumno} obtuvo {nota}")

if __name__ == "__main__":
    main()