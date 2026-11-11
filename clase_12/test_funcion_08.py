
from funcion_08 import *

# CONSIGNA: escribir pruebas usando solo assert.

def test_matriz_dos_filas():
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    resultado = sumar_matriz(matriz)

    assert resultado == 21


def test_matriz_vacia():
    matriz = []

    resultado = sumar_matriz(matriz)

    assert resultado == 0


def test_valores_negativos():
    matriz = [
        [-1, -2],
        [-3, -4]
    ]

    resultado = sumar_matriz(matriz)

    assert resultado == -10


def test_una_fila():
    matriz = [
        [10, 20, 30]
    ]

    resultado = sumar_matriz(matriz)

    assert resultado == 60
