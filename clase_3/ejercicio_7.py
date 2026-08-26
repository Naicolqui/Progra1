"""7. Conversión de tipos y formateo
Desarrollen un programa que solicite nombre del producto, precio unitario y cantidad. El precio deberá convertirse a float 
y la cantidad a int. Luego calculen el importe total.
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad
Muestren el resultado de dos maneras:
a) Utilizando una f-string y formato de dos decimales.
b) Utilizando concatenación; conviertan explícitamente los valores numéricos con str().
Comparen legibilidad, cantidad de conversiones necesarias y resultado obtenido."""

# Entradas de datos con conversión de tipos
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad

print(f"a) Producto: {producto} | Cantidad: {cantidad} | Precio U.: ${precio:.2f} | Total: ${total:.2f}")

print("b) Producto: " + producto + " | Cantidad: " + str(cantidad) + " | Precio U.: $" + str(precio) + " | Total: $" + str(total))