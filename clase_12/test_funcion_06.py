
from funcion_06 import *

# CONSIGNA: escribir pruebas usando solo assert.

def test_producto_existente():
    # ARRANGE
    stock = {"Frutillas": 50}
    producto = "Frutillas"
    cantidad = 10

    # ACT
    resultado = actualizar_stock(stock, producto, cantidad)

    # ASSERT
    assert resultado is True
    assert stock["Frutillas"] == 60


def test_producto_inexistente():
    # ARRANGE
    stock = {"Frutillas": 50}
    producto = "Mangos"
    cantidad = 10

    # ACT
    resultado = actualizar_stock(stock, producto, cantidad)

    # ASSERT
    assert resultado is False
    assert stock == {"Frutillas": 50}


def test_cantidad_negativa():
    # ARRANGE
    stock = {"Frutillas": 50}
    producto = "Frutillas"
    cantidad = -10

    # ACT
    resultado = actualizar_stock(stock, producto, cantidad)

    # ASSERT
    assert resultado is False
    assert stock["Frutillas"] == 50
