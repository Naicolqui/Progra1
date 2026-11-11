
from funcion_05 import *

# CONSIGNA: escribir pruebas usando solo assert.

def test_varios_mayores():
    numeros = [10, 20, 30, 40, 50]
    limite = 25

    resultado = contar_mayores(numeros, limite)

    assert resultado == 3


def test_ninguno():
    numeros = [1, 2, 3]
    limite = 10

    resultado = contar_mayores(numeros, limite)

    assert resultado == 0


def test_lista_vacia():
    numeros = []
    limite = 10

    resultado = contar_mayores(numeros, limite)

    assert resultado == 0


def test_igual_no_cuenta():
    numeros = [10, 20, 30]
    limite = 20

    resultado = contar_mayores(numeros, limite)

    assert resultado == 1
