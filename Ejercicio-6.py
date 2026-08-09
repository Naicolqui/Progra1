def calcularMulta(diasAtraso,estadoReserva):
    cargoFijo = 800
    montoReserva = 2500
    multa = cargoFijo*diasAtraso
    reserva = estadoReserva == 1  ##Se reasigna el valor de estadoReserva al preguntar si es igual a 1, 
    
    
    if reserva:
        totalMulta= multa + montoReserva

    else:
        totalMulta = multa
            
    return totalMulta


def mostrarResultado(importe):
    
    return print("El importe total de la multa  del usuario", nombre , "es: ",importe)


    
def cargarLista():
    listaMultas = []
    listaUsuarios = []
    sinMulta=0
    
    for i in range(3): # Modificar a 10

        estadoReserva = int(input("Indique el estado de la reserva 1 para reservado, 0 para sin reserva"))
        if estadoReserva == 1 or estadoReserva ==0 :
        
            diasAtraso = int(input("Ingrese los dias de atraso del usuario: "))
            nombre = input("Ingrese nombre del usuario a calcular")
            listaUsuarios.append(nombre)
        
        
            if diasAtraso > 0:
            
                importe = calcularMulta(diasAtraso,estadoReserva)
                listaMultas.append(importe)
                
            elif diasAtraso==0 or diasAtraso< 0:
                importe=0
                listaMultas.append(importe)
                sinMulta+=1
        
            
        
            else:
                print("Ingrese cantidad de dias valido.")
    
        else:
            print("Ingrese un estado de reserva valido")
        
        
        
    
    return listaMultas,listaUsuarios,sinMulta



    
def mayorMulta(listaMultas):
    mayor = listaMultas[0]
    for i in range (len(listaMultas)):
        if listaMultas[i] > mayor:
            mayor = listaMultas[i]
            
    return mayor

def calcularPromedio(listaMultas):
    contador=0
    for i in range(len(listaMultas)):
        contador+= listaMultas[i]
    promedio = contador/len(listaMultas)
    
    return promedio

            
def calcularLimite (listaMultas):
    limite = int(input("Ingrese el importe minimo a comparar: "))
    contador = 0
    for i in range (len(listaMultas)):
        if listaMultas[i]> limite:
            contador+=1
            
    return contador
        

    


def main():
    
    multa, usuario,sinMulta = cargarLista()
    print(usuario)
    print(multa)

    print("el listado de multas realizadas es: ",multa)
    print("La mayor multa registrada fue de: ",mayorMulta(multa))
    print("El promedio es: ", calcularPromedio(multa))
    print("el numero de usuarios que superan el valor limite indicado es" ,calcularLimite(multa))
    print("La cantidad de usuarios sin multa es: ,",sinMulta)
    
    


main()
