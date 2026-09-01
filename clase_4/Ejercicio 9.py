"""9. Desafío integrador: catálogo de productos
Desarrollen un programa modular que permita cargar productos. Cada producto se representará mediante una tupla
(codigo, descripcion, precio) y todos los productos se almacenarán en una lista. La carga finalizará cuando el código sea
"FIN".
Implementen las siguientes funciones:
• cargar_productos(): retorna la lista de tuplas cargadas.
• mostrar_productos(productos): muestra el catálogo.
• buscar_producto(productos, codigo): retorna la tupla encontrada o None.
• producto_mayor_precio(productos): retorna la tupla de mayor precio o None si la lista está vacía.
• precio_promedio(productos): retorna el promedio o None si no existen productos.
Durante la carga:
• No incorporen códigos repetidos.
• No intenten modificar una tupla existente. Para actualizar un precio, reemplacen en la lista el registro completo por una
nueva tupla."""


def cargar_productos():
    lista_productos=[]
    
    codigo=input("Ingrese el codigo de producto:  ")
    while codigo.lower() != 'fin':
        existe = False
        for producto in lista_productos:
            if producto[0] == codigo:
                existe = True

                if existe:
                    codigo=input("Ese codigo ya existe. Ingrese uno distinto.")
                    
        
           
        descripcion=input("Ingrese descripcion del producto:  ")
        precio=float(input("Ingrese el precio del producto:  "))
        producto=(codigo,descripcion,precio)
        lista_productos.append(producto)
        codigo=input("Ingrese el codigo de producto:  ")
    return lista_productos

def muestra_catalogo(lista_productos):
    for i in range(len(lista_productos)):
        print("Producto numero ",i+1,": " ,lista_productos[i])
    
    

def main():
    catalogo=cargar_productos()

    muestra_catalogo(catalogo)


main()



