import re

texto = """
Ana: ana@gmail.com - Tel: 1123456789 - Producto: PROD123
Juan: juan@gmail.com - Tel: 1198765432 - Producto: PROD456
María: maria@gmail.com - Tel: 1133344455 - Producto: PROD789
"""

# a) re.findall() → obtener todas las secuencias numéricas

numeros = re.findall(r"\d+", texto)

print("a) Secuencias numéricas:")
print(numeros)

print()

# b) re.finditer() → contenido, posición inicial y final
print("b) Coincidencias con finditer():")

coincidencias = re.finditer(r"\d+", texto)

for match in coincidencias:
    print("Contenido:", match.group())
    print("Inicio:", match.start())
    print("Fin:", match.end())
    print()


# c) Comparar el tipo de resultado

resultado_findall = re.findall(r"\d+", texto)
resultado_finditer = re.finditer(r"\d+", texto)

print("c) Tipos de resultado:")
print("findall:", type(resultado_findall))
print("finditer:", type(resultado_finditer))

print()


# d) findall() con grupos de captura
patron = r"(\w+)@(\w+)\.com"

resultado = re.findall(patron, texto)

print("d) findall() con grupos de captura:")
print(resultado)