""" 4. match, search y fullmatch
Los tres métodos devuelven un objeto Match cuando encuentran una coincidencia y None cuando no la encuentran. Antes
de utilizar group(), start(), end() o span(), es necesario comprobar que el resultado no sea None.
import re
patron = r"[A-Za-z][0-9]{3}"
codigo = "A123XYZ"
inicio = re.match(patron, codigo)
completo = re.fullmatch(patron, codigo)
Resolver:
a) Explicar por qué re.match() encuentra una coincidencia en el ejemplo.
b) Explicar por qué re.fullmatch() devuelve None.
c) Utilizar re.search() para localizar la primera secuencia numérica dentro de una frase.
d) Mostrar group(), start(), end() y span() solamente cuando exista una coincidencia.
e) Repetir una búsqueda con re.IGNORECASE.
re.match() comprueba únicamente desde el inicio de la cadena; no garantiza que todo el texto cumpla el patrón. Para
validar el formato completo, utilicen re.fullmatch() o un patrón correctamente anclado con ^ y $. """

import re




def main():
    patron = r"[A-Za-z][0-9]{3}"
    codigo = "A123XYZ"
    inicio = re.match(patron, codigo)
    completo = re.fullmatch(patron, codigo)

    if inicio:
        print("re.match() encontró una coincidencia:", inicio.group())
        ## match devuelve un objeto Match si el patrón coincide con el inicio de la cadena, por eso encuentra "A123".
    else:   
        print("re.match() no encontró una coincidencia.")

    if completo:
        print("re.fullmatch() encontró una coincidencia:", completo.group())
    else:
        print("re.fullmatch() no encontró una coincidencia.")
        ## fullmatch devuelve None porque el patrón no coincide con toda la cadena; "XYZ" no forma parte del patrón definido y en este caso debe coincidir en su totalidad.

    frase = "Me llamo Nicole y tengo 27 años."
    busqueda = re.search(r"\d+", frase)
    if busqueda:
        print("re.search() encontró una coincidencia:", busqueda.group())
        print("Inicio:", busqueda.start())
        print("Fin:", busqueda.end())
        print("Span:", busqueda.span())
    else:
        print("re.search() no encontró una coincidencia.")

    ##Repetir busqueda con ignorecase
    busqueda2 = re.search(r"[a-z]", frase, re.IGNORECASE)
    if busqueda2:
        print("re.search() con re.IGNORECASE encontró una coincidencia:", busqueda2.group())
        print("Inicio:", busqueda2.start())
        print("Fin:", busqueda2.end())
        print("Span:", busqueda2.span())
    else:
        print("re.search() con re.IGNORECASE no encontró una coincidencia.")

if __name__ == "__main__":
    main()