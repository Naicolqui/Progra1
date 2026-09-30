"""
Ejercicio 9. Desafío integrador: formulario de registro
Desarrollen un formulario que solicite nombre, legajo, correo electrónico, teléfono y código de comisión. Antes de
programar, definan y documenten el formato exacto de cada dato, especialmente el código de comisión.
El programa deberá:
• Validar el formato completo mediante funciones independientes.
• Mostrar un mensaje específico cuando un dato no cumpla el patrón.
• Volver a solicitar cada dato hasta obtener un valor válido.
• Mantener separadas la entrada de datos, la validación y la presentación de resultados.
• Mostrar al finalizar todos los datos registrados.
• Incluir un programa principal y un módulo validaciones.py.
• Código fuente de todos los ejercicios y del módulo validaciones.py.
• Tabla con cada patrón, su interpretación, alcance y ejemplos válidos e inválidos.
• Capturas de ejecución de match(), search(), fullmatch(), findall(), finditer(), sub() y split().
• Comparación entre búsqueda parcial y validación completa.

"""

import Validaciones as val

def pedir_nombre():
    nombre = input("Ingrese nombre del alumno, FIN para terminar: ").strip()
    while not val.validar_nombre(nombre):
        print("Nombre inválido, use solo letras.")
        nombre = input("Ingrese nombre del alumno, FIN para terminar: ").strip()
    return nombre


def pedir_legajo():
    legajo= input("Ingrese legajo (6 digitos numericos)")
    while not val.validar_legajo(legajo):
        print("Legajo invalido.")
        legajo= input("Ingrese legajo (6 digitos numericos)")
    return legajo


def pedir_mail():
    correo= input("Ingrese su correo(formato: nombre@mail.com): ")
    while not val.validar_correo(correo):
        print("correo invalido.")
        correo= input("Ingrese su correo, formato nombre@mail.com:  ")
    return correo

def pedir_comision ():
    comision= input("Ingrese comision:  ")
    while not val.validar_comision(comision):
        print("Comision invalida.")
        comision= input("Reingrese comision, formato correcto: A-XXXX: ")
    return comision


def pedir_telefono ():
    telefono= input("Ingrese telefono:  ")
    while not val.validar_telefono(telefono):
        print("telefono invalido.")
        telefono= input("Reingrese Telefono, formato correcto xx-xxxx-xxxx: ")
    return telefono

def mostrar_resultados(alumnos):
       
       if len (alumnos)==0:
           print("No hay datos de alumnos")
           
       else:
           print("\n--- Datos registrados ---")
           for i in range(len(alumnos)):
            print(f'Alumno ',i, alumnos[i])
       

        


def main():
    alumnos=[]
    nombre=pedir_nombre()
    while nombre.upper ()  != "FIN":
        legajo=pedir_legajo()
        correo=pedir_mail()
        comision=pedir_comision()
        telefono=pedir_telefono()
        alumnos.append((nombre,legajo,correo,comision,telefono))
        nombre=pedir_nombre()
    mostrar_resultados(alumnos)
main()



    

    





