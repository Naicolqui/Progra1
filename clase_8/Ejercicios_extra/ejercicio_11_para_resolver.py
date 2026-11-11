"""
EJERCICIO 11 - Para resolver

Dado el texto:
"Los productos tienen códigos AB123, XY999, abc123 y ZZ001"

Crear una expresión regular que encuentre solamente los códigos
formados por:
- 2 letras mayúsculas
- 3 números

Resultado esperado:
['AB123', 'XY999', 'ZZ001']
"""

import re

texto = "Los productos tienen códigos AB123, XY999, abc123 y ZZ001"

# Completar el patrón:
patron = r""

# re.findall() deberá utilizarse para obtener
# todos los códigos válidos.
# resultado = re.findall(patron, texto)
# print(resultado)


# Patrón: 2 letras mayúsculas seguidas de 3 números
patron = r"\b[A-Z]{2}\d{3}\b"

# Obtener todas las coincidencias
resultado = re.findall(patron, texto)

print(resultado)
