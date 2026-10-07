""" Crear un conjunto llamado tecnologías con al menos cuatro elementos y realizar:
a) Agregar una tecnología mediante add().
b) Eliminar una tecnología existente mediante remove().
c) Intentar eliminar una tecnología inexistente con remove() y registrar la excepción generada.
d) Repetir la operación con discard() y comparar el comportamiento.
e) Verificar con issubset() si las tecnologías obligatorias están incluidas en tecnologias.
f) Verificar con issuperset() la relación inversa.
g) Vaciar una copia del conjunto mediante clear(), sin perder el conjunto original.
remove() produce KeyError si el elemento no existe; discard() no produce una excepción en ese caso. Antes de utilizar
clear(), creen una copia con copy() para observar la diferencia entre ambos conjuntos. """

def main():
    tecnologias = {"Python", "Java", "Docker", "Git"}
    print("Conjunto inicial:", tecnologias)

    tecnologias.add("SQL")
    print("a) Despues de add('SQL'):", tecnologias)

    tecnologias.remove("Java")
    print("b) Despues de remove('Java'):", tecnologias)

    try:
        tecnologias.remove("Cobol")
    except KeyError as error:
        print("c) remove('Cobol') genero KeyError:", error)

    tecnologias.discard("Cobol")
    print("d) discard('Cobol') no produjo error:", tecnologias)

    obligatorias = {"Python", "Git"}
    print("e) obligatorias.issubset(tecnologias):", obligatorias.issubset(tecnologias))

    print("f) tecnologias.issuperset(obligatorias):", tecnologias.issuperset(obligatorias))

    copia = tecnologias.copy()
    copia.clear()
    print("g) Copia vaciada:", copia)
    print("   Original intacto:", tecnologias)

if __name__ == "__main__":
    main()

