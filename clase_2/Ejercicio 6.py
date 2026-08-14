
"""6. Listas por comprensión
Construyan nuevas listas sin utilizar append(). Distingan entre una transformación, un filtro y una expresión 
condicional.
puntajes = [45, 80, 63, 91, 100, 72]
a) Crear una lista con todos los puntajes duplicados.
b) Crear una lista que contenga solamente los puntajes aprobados (60 o más).
c) Crear una lista con el cuadrado de los valores pares.
d) Crear una lista con el texto "Aprobado" o "Revisar" según cada puntaje.
e) Explicar por qué la lista original no se modifica.
# Estructuras de referencia
[expresion for elemento in secuencia]
[expresion for elemento in secuencia if condicion]
[valor_si if condicion else valor_no for elemento in secuencia]""""


def duplicados(lista):
    #ejercicio a
    puntajesDuplicados=[i*2 for i in lista]

    return puntajesDuplicados

def aprobados(lista):
    #ejercicio b
    puntajesAprobados=[ i for i  in lista if i>60]

    return puntajesAprobados


def cuadradosPares(lista):
    #ejercicio c
    puntajesPares=[i**2 for i in lista if i%2==0]

    return puntajesPares


def revision(lista):
    #ejercicio d
    aRevisar= ["Aprob" if i>60 else "Desaprob" for i in lista ]
    return aRevisar

def main():
    puntajes = [45, 80, 63, 91, 100, 72]
    print(duplicados(puntajes))
    print(aprobados(puntajes))
    print(cuadradosPares(puntajes))
    print(revision(puntajes))

main()



"""
Ejercicio e
En los 3 casos, la lista original no se modifica, sino  que se recorre y utiliza como base para la generación de nuevas listas operando con los valores de cada posición, o evaluado una condición y devolviendo un valor por si o por no en la ultima condicion.
En ningún caso se toca la lista original sino que se genera una lista nueva.

"""