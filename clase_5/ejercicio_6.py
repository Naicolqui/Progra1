"""6. Cláusulas else y finally
Desarrollen un programa que solicite dos números y calcule su división. Utilicen:
• except ValueError para datos no numéricos.
• except ZeroDivisionError para un divisor igual a cero.
• else para mostrar el resultado solamente si el bloque try finalizó sin excepciones.
• finally para mostrar un mensaje de cierre que se ejecute exista o no un error.
El bloque else no reemplaza al try y finally no indica que la operación fue exitosa: solamente garantiza la ejecución de
tareas finales, como cerrar un recurso o informar que el intento terminó.
"""

try:
    valor_1 = int(input("Ingrese un valor: "))
    valor_2 = int(input("Ingrese otro valor: "))
    division = valor_1 / valor_2
    print(f"El resultado de la división es: {division}")
except ValueError:
    print("No se ingresó un número")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("La división se realizó correctamente")
finally:
    print("Fin del programa")
