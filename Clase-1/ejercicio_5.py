def calcular_multa(dias_atraso, esta_reservado):
    """Retorna el importe de la multa. esta_reservado es un valor booleano."""
    # Utilizo variables locales y no globales.
    multa_base = 800
    cargo_adicional = 2500

    if dias_atraso < 0:
        return 'Dias de atraso no puede ser negativo'
    if esta_reservado:
        return (dias_atraso * multa_base) + cargo_adicional
    return dias_atraso * multa_base


def mostrar_resultado(nombre_usuario, importe):
    """Muestra por pantalla el importe correspondiente a un usuario."""
    print(nombre_usuario, 'tiene una deuda de:', importe)


    # Programa principal
    nombre_usuario = input('Ingrese el nombre del cliente que realizó la reserva: ')
    dias_atraso = int(input('Ingrese los dias de atraso: '))
    respuesta_reserva = input('¿El libro estaba reservado? (S/N): ')
    # A partir del estado de reserva ingresado por el usuario caclulamos el booleano correspondiente.
    esta_reservado = bool(respuesta_reserva.strip().upper() == 'S')

    importe_final = calcular_multa(dias_atraso, esta_reservado)
    mostrar_resultado(nombre_usuario, importe_final)

    # Casos de prueba
    print('\nCasos de prueba:')
    mostrar_resultado('Caso 1 (3 dias, sin reserva)', calcular_multa(3, False))
    mostrar_resultado('Caso 2 (3 dias, con reserva)', calcular_multa(3, True))
    mostrar_resultado('Caso 3 (0 dias, sin reserva)', calcular_multa(0, False))
    mostrar_resultado('Caso 4 (-1 dias)', calcular_multa(-1, False))
