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
    
    codigo=input("Ingrese el codigo de producto, si ha terminado escriba fin:  ")
    while codigo.lower() != 'fin':
        existe = False
        for producto in lista_productos:
            if producto[0] == codigo:
                existe = True

                if existe:
                    codigo=input("Ese codigo ya existe. Ingrese uno distinto.")
                    
        
           
        descripcion=input("Ingrese descripcion del producto:  ")

        precio_valido = False
        while not precio_valido:
            try:
                precio=float(input("Ingrese el precio del producto:  "))
                if precio <= 0:
                    print("El precio debe ser mayor a cero.")
                else:
                    precio_valido = True
            except ValueError:
                print("Precio invalido. Ingrese solo numeros.")

        producto=(codigo,descripcion,precio)
        lista_productos.append(producto)
        codigo=input("Ingrese el codigo de producto:  ")
    return lista_productos

def muestra_catalogo(lista_productos):
    for i in range(len(lista_productos)):
        print("Producto numero ",i+1,": " ,lista_productos[i])
    
    

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto[0] == codigo:
            return producto
    return None

def producto_mayor_precio(productos):
    if not productos:
        return None

    mayor = productos[0]
    for producto in productos:
        if producto[2] > mayor[2]:
            mayor = producto
    return mayor

def precio_promedio(productos):
    if not productos:
        return None

    value = 0
    for producto in productos:
        value += producto[2]
    return value / len(productos)


def main():
    catalogo=cargar_productos()

    muestra_catalogo(catalogo)
    valor_promedio = precio_promedio(catalogo)
    print(f"El precio promedio es: {valor_promedio}")

    if catalogo:
        codigo_a_buscar = input("\nIngrese el código de producto a buscar: ")
        encontrado = buscar_producto(catalogo, codigo_a_buscar)
        
        if encontrado:
            print("Producto encontrado:", encontrado)
        else:
            print("No existe un producto con ese código.")

        mas_caro = producto_mayor_precio(catalogo)
        print("Producto de mayor precio:", mas_caro)


main()



