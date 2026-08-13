""" Una función lambda expresa una operación breve en una sola expresión. No reemplaza a una función def cuando se
necesitan varias instrucciones, validaciones complejas o documentación extensa.
Definan y prueben las siguientes funciones lambda:
a) cuadrado: retorna el cuadrado de un número.
b) es_par: retorna True cuando el número es par.
c) mayor: retorna el mayor entre dos números.
d) aplicar_descuento: aplica un descuento porcentual a un precio.
e) Indiquen cuál de ellas escribirían con def en un programa real y justifiquen. """

cuadrado = lambda a: a**2
es_par = lambda a: a % 2 == 0
mayor = lambda a, b: a if a > b else b
aplicar_descuento = lambda precio, porcentaje: precio - (precio * porcentaje / 100)


def main():
    print(cuadrado(4))
    print(es_par(4))
    print(mayor(3, 7))
    print(aplicar_descuento(100, 20))


if __name__ == "__main__":
    main()
