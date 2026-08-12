def calcular_multa(dias_atraso, esta_reservado):
    """Retorna el importe de la multa. esta_reservado es un valor booleano."""
    # Utilizo variables locales y no globales.
    multa_base = 800
    cargo_adicional = 2500

    if dias_atraso < 0:
        raise ValueError('Dias de atraso no puede ser negativo')
    if esta_reservado:
        return (dias_atraso * multa_base) + cargo_adicional
    return dias_atraso * multa_base

def multa_mayor(multas):
    mayor = multas[0]
    for multa in multas:
        if multa > mayor:
            mayor = multa

    return mayor

def promedio(multas):
    promedio = 0
    i = 1
    for multa in multas:
        promedio = (promedio + multa)/i
        i++
    
    return promedio

def limite_valor_multa(valor_limite):
    multas_limite = []
    for multa in multas:
        if multa > valor_limite:
            multas_limite.append(multa)

    return multas_limite

def lista_multas():
    multas = []

    for i in range(10):
        nombre_usuario = input('Ingrese el nombre del cliente que realizó la reserva: ')
        dias_atraso = int(input('Ingrese los dias de atraso: '))
        respuesta_reserva = input('¿El libro estaba reservado? (S/N): ')
        # A partir del estado de reserva ingresado por el usuario caclulamos el booleano correspondiente.
        esta_reservado = bool(respuesta_reserva.strip().upper() == 'S')

        importe = calcular_multa(dias_atraso, esta_reservado)

        multas.append(importe)

    return multas

#Programa ppal:
multas_finales = lista_multas();

print('Esta es la lista: ', multas_finales)
