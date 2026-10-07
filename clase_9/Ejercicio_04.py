"""
Dada una lista de códigos de alumnos que puede contener repeticiones, desarrollen una función codigos_unicos(codigos)
que retorne un conjunto con los códigos diferentes.
codigos = [101, 103, 101, 105, 103, 108]
unicos = set(codigos)

a) Informen cuántos códigos distintos hay.
b) Verifiquen si el código 105 fue informado.
c) Conviertan el conjunto en una lista ordenada para mostrar un resultado predecible.
d) Expliquen qué información se pierde al convertir directamente una lista en conjunto.

* Al convertir una lista en conjunto, se pierde el orden preestablecido en el punto c.

"""

def codigos_unicos(codigos):
    unicos = set(codigos)

    return unicos


#def codigos_informados (unico):


def main():
    codigos = [101, 103, 101, 105, 103, 108]
    unicos=codigos_unicos(codigos)
    print("Conjunto: ",unicos)
    if 105 in unicos:
        print("El codigo 105 existe en el conjunto")
    else:
        print("El codigo no existe")

    lista=list(unicos)
    lista_ordenada=lista.sort()

    print("lista: ",lista)


main()


