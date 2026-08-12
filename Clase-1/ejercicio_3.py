cargo_adicional = 2500
multa_base = 800

def calculo_multa(dias_atraso, estado_reserva):
    if dias_atraso < 0:
        return 'Dias de atraso no puede ser negativo'
    if estado_reserva:
        return (dias_atraso * multa_base) + cargo_adicional
    return dias_atraso * multa_base


salida = calculo_multa(0, False)
salida2 = calculo_multa(0, True)
salida3 = calculo_multa(2, False)
salida4 = calculo_multa(2, True)
salida5 = calculo_multa(-1, False)

print('El usuario debe $', salida)
print('El usuario debe $', salida2)
print('El usuario debe $', salida3)
print('El usuario debe $', salida4)
print('El usuario debe $', salida5)
