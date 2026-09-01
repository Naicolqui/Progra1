"""
4. Acceso, recorrido y rebanadas"""
productos = ("Teclado", "Mouse", "Monitor", "Auriculares", "Webcam")

# Resolver:
# a) Mostrar el primer, el último y el elemento central.
tot_elementos = len(productos)
print("Primer elemento:", productos[0])
print("Último elemento:", productos[-1])
if tot_elementos % 2 == 1:
    print("Elemento central:", productos[tot_elementos // 2])


# b) Obtener los tres primeros elementos.
print("Tres primeros elementos:", productos[:3])

# c) Obtener los elementos desde "Monitor" hasta el final.
print("Elementos desde 'Monitor' hasta el final:", productos[2:])

# d) Crear una nueva tupla con el orden invertido.
productos_invertidos = productos[::-1]
print("Tupla invertida:", productos_invertidos)

# e) Recorrerla con for e informar cada producto.
for producto in productos:
    print("Producto:", producto)

# f) Intentar ejecutar productos[0] = "Notebook" e interpretar el error.
#productos[0] = "Notebook" 
#print("Intentando modificar la tupla:", productos)# devuelve TypeError: 'tuple' object does not support item assignment
"""lo que quiza podria hacerse para agregar ese elemento es crear una nueva tupla con el elemento agregado, ya que las tuplas son inmutables. Por ejemplo:"""
productos = productos + ("Notebook" ,)
print("Tupla después de agregar 'Notebook':", productos)

"""Las rebanadas retornan una nueva tupla; no modifican la original. Comprueben que productos conserva su contenido 
después de cada operación."""
