from funcion_05 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: varios mayores, ninguno, lista vacia, igual no cuenta.

def test_varios_mayores():
    assert contar_mayores([1, 5, 8, 10], 4) == 3
    assert contar_mayores([10, 20, 30], 0) == 3

def test_ninguno():
    assert contar_mayores([1, 2, 3], 10) == 0

def test_lista_vacia():
    assert contar_mayores([], 5) == 0

def test_igual_no_cuenta():
    assert contar_mayores([5, 5, 5], 5) == 0
    assert contar_mayores([3, 5, 7], 5) == 1
