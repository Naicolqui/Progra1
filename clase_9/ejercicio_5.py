alumnos = {
    1001: "Ana",
    1002: "Bruno",
    1003: "Carla"
}

diccionario_vacio = {}

# a) ¿Qué representa cada clave y cada valor?
print("a) Las claves representan los números de identificación de los alumnos.")
print("   Los valores representan los nombres de los alumnos.")

# b) ¿Qué ocurriría si se volviera a asignar un valor a la clave 1002?
alumnos[1002] = "Pedro"

print("b) Si se asigna otro valor a la clave 1002, se reemplaza el valor anterior.")
print(alumnos)

# c) ¿Por qué una lista no puede utilizarse como clave?
print("c) Una lista no puede utilizarse como clave porque es mutable y no es hashable.")

# d) ¿Qué diferencia existe entre {} y set()?
print("d) {} representa un diccionario vacío.")
print("   set() representa un conjunto vacío.")

print("Diccionario vacío:", diccionario_vacio)
print("Conjunto vacío:", set())