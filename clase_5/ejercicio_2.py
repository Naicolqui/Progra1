""" 2. Ciclos controlados con while True
while True crea un ciclo cuya condición siempre es verdadera. Debe utilizarse solamente cuando la condición de
finalización se comprueba dentro del bloque y conduce de manera clara a un break.
Desarrollen un programa que solicite números enteros y finalice cuando se ingrese -1. El valor -1 es la condición a
controlar: controla la finalización y no debe incorporarse a los cálculos.
Al finalizar, informar cantidad, suma y promedio. Si el primer valor ingresado es -1, mostrar que no existen datos para
calcular el promedio. No utilicen while True para reemplazar un for cuando la cantidad de repeticiones ya se conoce. """

def numeros_enteros():
    cantidad = 0
    suma = 0

    while True:
        try:
            numero = int(input("Ingrese un número entero (-1 para finalizar): "))
            if numero == -1:
                break
            cantidad += 1
            suma += numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    if cantidad > 0:
        promedio = suma / cantidad

        return cantidad, suma, promedio
        
    else:
        print("No existen datos para calcular el promedio.")

def main():
    cantidad, suma, promedio = numeros_enteros()

    print(f"Cantidad de números ingresados: {cantidad}")
    print(f"Suma de los números: {suma}")
    print(f"Promedio de los números: {promedio}")

if __name__ == "__main__":
    main()