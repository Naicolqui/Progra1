
from funcion_02 import *

# CONSIGNA: escribir pruebas usando solo assert.

def test_numero_par():
    assert es_par(4) == True

def test_numero_impar():
    assert es_par(5) == False

def test_cero():
    assert es_par(0) == True
