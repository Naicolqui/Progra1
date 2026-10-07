# EJERCICIO 9 - Verificar pertenencia
#
# Dado el siguiente conjunto:

# Pedir al usuario un nombre de usuario.
# Informar si el usuario está registrado o no.

# Escribí tu solución debajo de esta línea:

def main():
    usuarios_registrados = {"ana", "pedro", "maria", "juan"}

    nombre_usuario = input("Ingrese un nombre de usuario: ")

    if nombre_usuario in usuarios_registrados:
        print(f"El usuario '{nombre_usuario}' está registrado.")
    else:
        print(f"El usuario '{nombre_usuario}' no está registrado.")

if __name__ == "__main__":
    main()