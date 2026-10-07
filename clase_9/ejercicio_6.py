""" Utilizando el diccionario alumnos, resolver:
a) Mostrar el nombre asociado al legajo 1002 mediante alumnos[1002].
b) Agregar el legajo 1004 y luego modificar el nombre asociado al legajo 1001.
c) Verificar con in si existe el legajo 1010.
d) Consultarlo con get() y un mensaje alternativo.
e) Intentar acceder directamente a la clave inexistente y capturar KeyError.
f) Eliminar un legajo existente con del, luego de comprobar su existencia.
nombre = alumnos.get(1010, "Legajo inexistente")
print(nombre)
El operador in aplicado a un diccionario consulta sus claves. get() permite obtener un valor sin generar KeyError cuando la 
clave no existe. La asignación diccionario[clave] = valor agrega un par nuevo o reemplaza el valor si la clave ya estaba 
registrada"""

def main():
    alumnos = {
        1001: "Ana",
        1002: "Bruno",
        1003: "Carla"
    }

    print("a) Legajo 1002:", alumnos[1002])

    alumnos[1004] = "Diego"
    alumnos[1001] = "Ana Maria"
    print("b) Diccionario actualizado:", alumnos)

    print("c) Existe el legajo 1010:", 1010 in alumnos)

    nombre = alumnos.get(1010, "Legajo inexistente")
    print("d) Legajo 1010:", nombre)

    try:
        print(alumnos[1010])
    except KeyError as error:
        print("e) KeyError, no existe la clave:", error)

    if 1003 in alumnos:
        del alumnos[1003]
        print("f) Legajo 1003 eliminado:", alumnos)
    else:
        print("f) El legajo 1003 no existe")

if __name__ == "__main__":
    main()

