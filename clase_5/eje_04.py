
""" 
4. Captura con try-except
El bloque try contiene únicamente las instrucciones que pueden generar el error esperado. Cada except debe capturar una 
excepción específica. Eviten except sin tipo, porque oculta la causa del problema y dificulta la depuración.
Modifiquen el ejercicio del punto 3 para capturar ValueError cuando el usuario ingrese un dato no entero. El programa 
deberá informar el error y continuar solicitando valores sin perder los datos válidos ya cargados. """ 

try:
    numero = int(input("Ingrese un número: "))
    resultado = 100 / numero
    print(resultado)
except (ValueError,ZeroDivisionError ):
    print("Error: debe ingresar un número entero. Intente de nuevo.")


