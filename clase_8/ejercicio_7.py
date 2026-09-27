""" Implementen funciones que reciban una cadena y retornen True o False. Para comprobar el formato completo, utilicen
re.fullmatch().
Ing Maria Eugenia Varando
import re
def validar_legajo(legajo):
 return re.fullmatch(r"[0-9]{5}", legajo) is not None
def validar_codigo(codigo):
 return re.fullmatch(r"[A-Z]{2}[0-9]{4}", codigo) is not None
Completen también:
a) validar_telefono(telefono): cuatro dígitos, guion y cuatro dígitos.
b) validar_correo(correo): usuario, @, dominio y extensión de al menos dos letras.
c) validar_importe(importe): símbolo $ seguido por uno o más dígitos.
d) validar_patente(patente): uno de los dos formatos analizados en la sección 4.
La expresión de correo propuesta en clase es una aproximación didáctica y no representa todas las direcciones válidas
posibles. Prueben cada función con, como mínimo, tres casos válidos, tres inválidos y una cadena vacía. """

import re


def validar_legajo(legajo):
 return re.fullmatch(r"[0-9]{5}", legajo) is not None

def validar_codigo(codigo):
 return re.fullmatch(r"[A-Z]{2}[0-9]{4}", codigo) is not None

def validar_telefono(telefono):
 return re.fullmatch(r"[0-9]{2,4}-[0-9]{8}", telefono) is not None

def validar_correo(correo):
 return re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", correo) is not None

def validar_importe(importe):
 return re.fullmatch(r"\$[0-9]+", importe) is not None

def validar_patente(patente):
 return re.fullmatch(r"[A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2}", patente) is not None

def main():
    print(validar_legajo("12345"))
    print(validar_legajo("1234"))
    print(validar_legajo("123456"))
    print(validar_legajo(""))

    print(validar_codigo("AB1234"))
    print(validar_codigo("A1234"))
    print(validar_codigo("AB12345"))
    print(validar_codigo(""))

    print(validar_telefono("1234-5678"))
    print(validar_telefono("123-4567"))
    print(validar_telefono("12345-6789"))
    print(validar_telefono(""))

    print(validar_correo("user@example.com"))
    print(validar_correo("user@example"))
    print(validar_correo("user@.com"))
    print(validar_correo(""))    

    print(validar_importe("$123"))
    print(validar_importe("123"))
    print(validar_importe("$"))
    print(validar_importe(""))

    print(validar_patente("ABC123"))
    print(validar_patente("AB123C"))
    print(validar_patente("AB1234"))
    print(validar_patente(""))

if __name__ == "__main__":
    main()