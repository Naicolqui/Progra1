""" 8. Comprobaciones internas con assert
assert comprueba una condición que el programador espera que siempre sea verdadera. Si resulta falsa, genera
AssertionError. Es una ayuda para detectar errores de lógica o verificar invariantes internas; no debe utilizarse como
mecanismo principal para validar datos ingresados por el usuario, ya que las aserciones pueden desactivarse.
importe = calcular_importe(3, 1200)
assert importe == 3600, "El importe calculado no es el esperado"
Escriban otras dos aserciones: una que verifique un caso correcto y otra que falle intencionalmente. Interpreten el
mensaje de AssertionError obtenido. """

def calcular_importe(cantidad, precio_unitario):
    return cantidad * precio_unitario

def main():
    # Caso correcto
    importe = calcular_importe(3, 1200)
    assert importe == 3600, "El importe calculado no es el esperado"

    # Caso que falla intencionalmente
    importe = calcular_importe(2, 1000)
    assert importe == 3000, "El importe calculado no es el esperado"

if __name__ == "__main__":
    main()