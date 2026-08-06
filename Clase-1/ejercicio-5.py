multa_base = 800
cargo_adicional = 2500

def calcular_multa(dias_atraso, reservado):
    if dias_atraso < 0:
        return 'Dias de atraso no puede ser negativo'
    if reservado:
        return (dias_atraso * multa_base) + cargo_adicional
    return dias_atraso * multa_base

def mostrar_resultado(nombre_usuario, importe):
    """Muestra el importe correspondiente a un usuario."""
    return nombre_usuario + ' tiene una deuda de: ' + str(importe)

importe_final = calcular_multa(3, True)
respuesta = mostrar_resultado('Nicole', importe_final)
print(respuesta)