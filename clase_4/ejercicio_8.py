""" a) Total vendido por producto
b) Total de una semana indicada
c) Código del producto con mayor venta
d) Validar semana e capturar errores """

def total_vendido(ventas):
    total_ventas = ()
    for venta in ventas:
        total_ventas += (sum(venta),)

    return total_ventas

def cargar_ventas(codigos, cantidad_semanas=4):
    ventas = []
    for producto in codigos:
        semanas = [0] * cantidad_semanas
        for i in range(cantidad_semanas):
            semana = validar_semana(1, cantidad_semanas, f"Ingrese el número de semana a cargar para {producto}: ")
            valor_valido = False
            while valor_valido == False:
                valor_texto = input(f"Ingrese venta de {producto} - semana {semana}: ")
                if valor_texto.isdigit():
                    semanas[semana - 1] = int(valor_texto)
                    valor_valido = True
                else:
                    print("El valor de venta debe ser un número")
        ventas.append(semanas)

    return ventas

def validar_semana(limite_inferior, limite_superior, texto):
    valido = False
    while valido == False:
        valor = input(texto).strip()
        if valor.isdigit():
            valor = int(valor)
            if valor >= limite_inferior and valor <= limite_superior:
                valido = True
            else:
                print("La semana debe estar entre", limite_inferior, "y", limite_superior)
        else:
            print("Debe ingresar un número entero")
    return valor

def mas_vendido(ventas, codigos):
    maximo = max(ventas)
    for i, venta in enumerate(ventas): ##Control de indexado, por cada "vuelta" le asigna el indice correspondiente
        if venta == maximo:
            return codigos[i]

def main():
    codigos = ("P101", "P205", "P330")
    ventas_semanales = cargar_ventas(codigos)

    total_ventas = total_vendido(ventas_semanales)
    i = 0
    for venta in total_ventas:
        print(f"{codigos[i]} vendió esta semana: {venta}")
        i += 1

    print(f"El producto mas vendido fue: {mas_vendido(ventas_semanales, codigos)}")

if __name__ == "__main__":
    main()
