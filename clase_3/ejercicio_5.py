""" a) Mostrar el primer y el último carácter.
b) Obtener la palabra "Programacion" mediante slicing.
c) Mostrar la cadena invertida.
d) Verificar si la palabra "Python" pertenece a la cadena.
e) Intentar modificar texto[0] y explicar el error obtenido. """

def mostrarCaracter(frase):
    print("Esta es la primer letra:", frase[0])
    print("Esta es la segunda letra: ", frase[-1])

def obtenerProgramacion():
    frase = "Esta es una clase de Programación"
    print(" Esta es tu palabra: ", frase[21:], "porque la frase es: ", frase)

def findPython(frase):
    print("Contiene Python siendo case sensitive:", "Python" in frase)
    print("Contiene Python sin ser case sensitive:", "python" in frase.lower())

def modifyWord(frase):
    # frase[0] = "o"
    print("La frase: ", frase, "-> No se puede modificar dado que no se puede modificar una cadena existente por posición. Son INMUTABLES.")


def main():
    print("Ingrese una frase cualquiera: ")
    frase = input()
    mostrarCaracter(frase)
    obtenerProgramacion()
    findPython(frase)
    modifyWord(frase)

if __name__ == "__main__":
    main()

