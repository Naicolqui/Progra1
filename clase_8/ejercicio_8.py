import re

# Texto de prueba
texto = """
Contacto 1:
Correo: ana@gmail.com
Teléfono: 1234-5678
Código de producto: AB1234

Contacto 2:
Correo: juan.perez@hotmail.com
Teléfono: 4567-8910
Código de producto: XY5678

Otros datos:
Edad: 25
Código incorrecto: A1234
Teléfono incorrecto: 12345678
Correo incorrecto: juan@hotmail
"""

print("TEXTO DE PRUEBA")
print(texto)
print("=" * 60)


# ==========================================================
# a) Encontrar todas las coincidencias de cada tipo
# ==========================================================

# Correo electrónico
patron_correo = r"\w+([.-]?\w+)*@\w+([.-]?\w+)*\.\w+"

# Teléfono con formato 1234-5678
patron_telefono = r"\d{4}-\d{4}"

# Código con formato AB1234
patron_codigo = r"[A-Z]{2}\d{4}"


correos = re.findall(patron_correo, texto)
telefonos = re.findall(patron_telefono, texto)
codigos = re.findall(patron_codigo, texto)


print("a) COINCIDENCIAS")
print("Correos:", correos)
print("Teléfonos:", telefonos)
print("Códigos:", codigos)

print()


# ==========================================================
# b) Cantidad encontrada
# ==========================================================

print("b) CANTIDAD ENCONTRADA")
print("Cantidad de correos:", len(correos))
print("Cantidad de teléfonos:", len(telefonos))
print("Cantidad de códigos:", len(codigos))

print()


# ==========================================================
# c) Posición inicial y final con finditer()
# ==========================================================

print("c) POSICIONES")
print()

print("CORREOS:")
for match in re.finditer(patron_correo, texto):
    print(
        "Contenido:", match.group(),
        "| Inicio:", match.start(),
        "| Fin:", match.end()
    )

print()

print("TELÉFONOS:")
for match in re.finditer(patron_telefono, texto):
    print(
        "Contenido:", match.group(),
        "| Inicio:", match.start(),
        "| Fin:", match.end()
    )

print()

print("CÓDIGOS:")
for match in re.finditer(patron_codigo, texto):
    print(
        "Contenido:", match.group(),
        "| Inicio:", match.start(),
        "| Fin:", match.end()
    )