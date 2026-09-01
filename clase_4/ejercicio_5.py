# b)
def verificar_elementos(ventas):
    esta_150 = 150 in ventas
    ausente_500 = 500 not in ventas
    return esta_150, ausente_500

# c)
def contar_apariciones(ventas, elemento):
    return ventas.count(elemento)

# d)
def buscar_posicion(ventas, elemento):
    if elemento in ventas:
        return ventas.index(elemento)
    else:
        return f"El elemento {elemento} no se encuentra en la tupla."


def concatenar(ventas):
    tupla2 = (4, 5, 6)
    nueva_tupla = ventas + tupla2

    return nueva_tupla


def replicar():
    tupla = (1, 2, 3)
    tupla_replicada = tupla * 3
    return tupla_replicada


def main():

    ventas = (120, 85, 230, 150, 90, 150)

    # b)
    esta_150, ausente_500 = verificar_elementos(ventas)
    print(f"b) ¿150 está en ventas?: {esta_150} | ¿500 está ausente?: {ausente_500}")

    # c)
    apariciones = contar_apariciones(ventas, 150)
    print(f"c) El número 150 aparece {apariciones} veces.")

    # d)
    pos_230 = buscar_posicion(ventas, 230)
    print(f"d) Posición de 230: {pos_230}")

    nueva_tupla = concatenar(ventas)

    print("Tupla concatenada exitosamente: ", nueva_tupla)
    
    tupla_replicada = replicar()

    print("Tupla replicada:", tupla_replicada)

if __name__ == "__main__":
    main()

