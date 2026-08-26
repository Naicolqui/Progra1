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
    nueva_tupla = concatenar(ventas)

    print("Tupla concatenada exitosamente: ", nueva_tupla)
    
    tupla_replicada = replicar()

    print("Tupla replicada:", tupla_replicada)

if __name__ == "__main__":
    main()

