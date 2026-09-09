"""7. Provocar una excepción con raise

raise permite señalar que un dato no cumple las reglas del problema, aun cuando su tipo sea correcto. 
Implementen calcular_importe(cantidad, precio) de modo que provoque ValueError si cantidad o precio son menores iguales a cero. 
La función deberá retornar cantidad * precio cuando los datos sean válidos.
Desde el programa principal, capturen la excepción y muestren su mensaje utilizando except ValueError as error.
Prueben con datos válidos, cantidad cero, precio negativo y entradas no numéricas """

def calcular_importe(cantidad, precio):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a cero")
    
    return cantidad * precio


def main():
    try:
        cantidad = float(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        importe = calcular_importe(cantidad, precio)
        print("El importe es:", importe)
    except ValueError as error:
        print("Error:", error)


main()



