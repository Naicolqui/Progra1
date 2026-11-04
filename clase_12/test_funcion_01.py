from funcion_01 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: suma positivos, suma negativos, suma cero.

def test_suma_positivos():
    assert sumar(10, 20) == 30
    pass

def test_suma_negativos():
    assert sumar(-1, -3) == -4
    pass

def test_suma_cero():
    assert sumar(1, -1) == 0
    assert sumar(5, 0) == 5
    pass
