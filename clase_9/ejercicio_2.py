grupo_a = {101, 102, 103, 104, 105}

grupo_b = {104, 105, 106, 107}

# a) Unión
resultado = grupo_a | grupo_b
print(resultado)

# b) Intersección
resultado = grupo_a & grupo_b
print(resultado)

# c) Diferencia
resultado = grupo_a - grupo_b
print(resultado)

resultado = grupo_b - grupo_a
print(resultado)

# d) Diferencia simétrica
resultado = grupo_a ^ grupo_b
print(resultado)

# e) Pertenencia
resultado = 103 in grupo_a
print(resultado)

resultado = 108 not in grupo_b
print(resultado)

# f) La diferencia no es una operación conmutativa
resultado_1 = grupo_a - grupo_b
resultado_2 = grupo_b - grupo_a

print(resultado_1)
print(resultado_2)