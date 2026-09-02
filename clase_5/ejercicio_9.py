"""9. Desafío integrador: carga segura de productos 
Desarrollen un sistema modular que registre productos en una lista. Cada producto podrá almacenarse como una lista con 
código, descripción, cantidad y precio. La carga finaliza cuando el código ingresado sea "FIN". 
El programa deberá: 
• Utilizar while True y break para finalizar la carga. 
• Capturar ValueError al convertir cantidad y precio. 
• Utilizar raise ValueError para rechazar cantidades o precios menores o iguales a cero. 
• No incorporar un producto cuando sus datos sean inválidos. 
• Calcular el importe de cada producto mediante una función. 
• Utilizar assert para comprobar una condición interna del cálculo, no para validar la entrada. 
• Informar cantidad de productos, importe total y precio promedio; si no se cargaron productos, evitar la división por 
cero."""

def cargar_productos():
    lista_productos = []
    
    while True:
        codigo = input("Ingrese el código del producto (o 'FIN' para finalizar): ")
        if codigo.upper() == "FIN":
            break
        
        descripcion = input("Ingrese la descripción del producto: ")
        
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero.")
        except ValueError as e:
            print(f"Error: {e}")
            continue
        
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a cero.")
        except ValueError as e:
            print(f"Error: {e}")
            continue
        
        producto = [codigo, descripcion, cantidad, precio]
        lista_productos.append(producto)
    
    return lista_productos

#main
carga = cargar_productos()
print("Productos cargados:", carga)