from funcion_04 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: mayusculas, espacios, vacio.

#def normalizar(texto):
# return texto.strip().lower()

def test_mayusculas():
    assert normalizar("HOLA") == "hola"
    assert normalizar("HoLa MuNdO") == "hola mundo"
    pass

def test_espacios():
    assert normalizar("hola  ") == "hola"
    assert normalizar("  Error 404  ") == "error 404"
    pass

def test_vacio():
    assert normalizar("") == ""
    assert normalizar("      ") == ""
    pass

