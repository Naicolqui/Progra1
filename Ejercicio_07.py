"""
7. Recorridos de diccionarios


Resolver:
a) Recorrer directamente el diccionario y mostrar sus claves.
b) Mostrar las cantidades mediante values().
c) Mostrar cada producto y su stock mediante items().
d) Informar la cantidad de productos diferentes con len().
e) Calcular el total de unidades disponibles.
f) Informar el producto con mayor stock mediante max(stock, key=stock.get).
La expresión max(stock.values()) devuelve la mayor cantidad, pero no identifica el producto. Para obtener la clave
asociada al mayor valor puede utilizarse max(stock, key=stock.get). Analicen qué ocurriría si el diccionario estuviera vacío
o si dos productos compartieran la cantidad máxima.


De existir dos productos con la misma cantidad, la expresion max(stock.key=stock.get) muestra la primer llave encontrada.Si el diccionario esta vacio, devuelve el error

ValueError: max() iterable argument is empty 



"""
contador=0
stock = {
"teclado": 20,
"mouse": 20,
"monitor": 7,
"webcam": 5
}
# a) Recorrer directamente el diccionario y mostrar sus claves.
for caracteristicas in stock:
    print(caracteristicas)
#b) Mostrar las cantidades mediante values().  
#e) Calcular el total de unidades disponibles.
for cantidad in stock.values():
    contador+=cantidad
    print(cantidad)

print("Cantidad total de elementos: ",contador)


#c) Mostrar cada producto y su stock mediante items().

for caracteristicas in stock.items():
    print("Articulo: ",caracteristicas)


#d) Informar la cantidad de productos diferentes con len().
print("Cantidad de elementos del diccionario:", len(stock))
#f) Informar el producto con mayor stock mediante max(stock, key=stock.get).
print("Articulo con mayor cantidad de unidades en stock: ",max(stock, key=stock.get))



    