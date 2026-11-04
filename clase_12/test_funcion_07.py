from funcion_07 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: clave valida, clave corta, sin numeros, limite ocho.

def test_clave_valida():
    
    assert clave_valida("abcdef12345") == True
    pass

def test_clave_corta():
    assert clave_valida("abc123") == False
    assert clave_valida("clave") == False
    pass

def test_sin_numeros():
    assert clave_valida("abcdefghijk") == False
    pass

def test_limite_ocho():
    assert clave_valida("abc12345") == True
    assert clave_valida("abc1238") == False
    pass
