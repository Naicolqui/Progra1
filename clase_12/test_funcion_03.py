from funcion_03 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: descuento normal, sin descuento, descuento total, descuento invalido.


from funcion_03 import *

# CONSIGNA: escribir pruebas usando solo assert.

def test_descuento_normal():
    # ARRANGE
    precio = 100
    descuento = 20

    # ACT
    resultado = precio_final(precio, descuento)

    # ASSERT
    assert resultado == 80


def test_sin_descuento():
    # ARRANGE
    precio = 100
    descuento = 0

    # ACT
    resultado = precio_final(precio, descuento)

    # ASSERT
    assert resultado == 100


def test_descuento_total():
    # ARRANGE
    precio = 100
    descuento = 100

    # ACT
    resultado = precio_final(precio, descuento)

    # ASSERT
    assert resultado == 0


def test_descuento_invalido():
    # ARRANGE
    precio = 100
    descuento = 150

    # ACT
    resultado = precio_final(precio, descuento)

    # ASSERT
    assert resultado == -1
