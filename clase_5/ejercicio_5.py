""" 5. Múltiples excepciones y reglas del problema
numeros = [10, 20, 30, 40]
posicion = int(input("Posición: "))
print(numeros[posicion])
Capturen ValueError cuando el dato no pueda convertirse a entero e IndexError cuando la posición quede fuera del rango
de la lista. Recuerden que los índices negativos son válidos en Python; si la regla del problema solo permite posiciones
entre 0 y len(numeros)-1, deberán validarlo expresamente y provocar un ValueError.
Prueben con "dos", 1, 8 y -1. Expliquen por qué conviene mostrar un mensaje diferente para cada problema. """

def carga_datos():
    numeros = [10, 20, 30, 40]
    try:
        posicion = int(input("Posición: "))
        if posicion < 0 or posicion >= len(numeros):
            raise ValueError("La posición debe estar entre 0 y {}.".format(len(numeros)-1))
        print(numeros[posicion])
    except ValueError as e:
        print("Error de valor:", e)
    except IndexError:
        print("Error de índice: La posición está fuera del rango de la lista.")

def main():
    carga_datos()

if __name__ == "__main__":
    main()