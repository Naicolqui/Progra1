# EJERCICIO 1 - Diccionario básico
#
# Crear un diccionario llamado alumno con las siguientes claves:
# "nombre", "edad" y "carrera".
# Luego mostrar por pantalla el nombre y la carrera del alumno.

# Escribí tu solución debajo de esta línea:


def main():

    alumno = {
        "nombre": "Nicole Quilmore",
        "edad": 27,
        "carrera": "Lic. en Sistemas"
    }

    print("Nombre:", alumno["nombre"])
    print("Carrera:", alumno["carrera"])

if __name__ == "__main__":
    main()