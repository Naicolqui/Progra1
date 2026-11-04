
from funcion_09 import *

# CONSIGNA: escribir pruebas usando solo assert.

def test_dos_productos():
    # ARRANGE
    ventas = [
        ("Frutillas", 2, 100),
        ("Frambuesas", 3, 200)
    ]

    # ACT
    resultado = resumen_ventas(ventas)

    # ASSERT
    assert resultado == {
        "Frutillas": 200,
        "Frambuesas": 600
    }


def test_producto_repetido():
    # ARRANGE
    ventas = [
        ("Frutillas", 2, 100),
        ("Frutillas", 3, 100)
    ]

    # ACT
    resultado = resumen_ventas(ventas)

    # ASSERT
    assert resultado == {"Frutillas": 500}


def test_sin_ventas():
    # ARRANGE
    ventas = []

    # ACT
    resultado = resumen_ventas(ventas)

    # ASSERT
    assert resultado == {}


def test_venta_cero():
    # ARRANGE
    ventas = [
        ("Frutillas", 0, 100)
    ]

    # ACT
    resultado = resumen_ventas(ventas)

    # ASSERT
    assert resultado == {"Frutillas": 0}
