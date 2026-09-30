import re

# Texto de prueba
texto = "Hola mundo. Mi edad es 24 años. Mi DNI es 12345678. Hoy es septiembre."
print("TEXTO:")
print(texto)
print("-" * 50)

# a) ^ y $ → inicio y final de la cadena
print("a) ^ y $")
print(re.search(r"^Hola", texto))
print(re.search(r"septiembre\.$", texto))
print()

# b) . → cualquier carácter excepto salto de línea
print("b) .")
print(re.findall(r"c.sa", "casa cosa cesa"))
print()

# c) [ ] → clase de caracteres
print("c) [ ]")
print(re.findall(r"[0-9]", "Tengo 24 años"))
print(re.findall(r"[A-Z]", "Hola MUNDO Python"))
print()

# d) [^ ] → negación

print("d) [^ ]")

print(re.findall(r"[^0-9]", "Hola123"))
print()


# e) | → alternativas

print("e) |")

print(re.findall(r"rojo|azul", "El auto es rojo y la casa es azul"))
print()


# f) ( ) → agrupación

print("f) ( )")

print(re.findall(r"(ha)+", "ha hahaha hahahaha"))
print()


# g) ?, * y + → cuantificadores

print("g) ?, * y +")

# ? → cero o una repetición
print(re.findall(r"colou?r", "color colour"))

# * → cero o más repeticiones
print(re.findall(r"ab*", "a ab abb abbb"))

# + → una o más repeticiones
print(re.findall(r"ab+", "a ab abb abbb"))
print()


# h) {m}, {m,n} y {m,} → cantidad de repeticiones

print("h) {m}, {m,n} y {m,}")

# {m} → exactamente m veces
print(re.findall(r"\d{4}", "123 1234 12345"))

# {m,n} → entre m y n veces
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))

# {m,} → m o más veces
print(re.findall(r"\d{3,}", "1 12 123 1234 12345"))
print()


# i) \ → escape de un metacarácter

print("i) \\")

# El punto normalmente significa "cualquier carácter".
# Con \. buscamos un punto literal.

print(re.findall(r"\.", "Hola. ¿Cómo estás?"))
print()


# IMPORTANTE: | vs [ ]

print("Diferencia entre | y [ ]")

print("(septiembre|setiembre):")
print(re.findall(r"(septiembre|setiembre)",
                 "septiembre setiembre"))

print()

print("[septiembre|setiembre]:")
print(re.findall(r"[septiembre|setiembre]",
                 "septiembre"))