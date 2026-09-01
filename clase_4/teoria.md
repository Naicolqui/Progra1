**Ejercicio 1:**

¿Qué significa que un objeto sea mutable o inmutable?

Un objeto es mutable cuando se puede modificar su contenido después de haberlo creado, sin necesidad de generar uno nuevo. A diferencia de un objeto inmutable, el cual una vez creado no se puede alterar.

**Ejercicio 2:**

d) Un ejemplo de tupla podria ser una fecha de cumpleaños de un usuario, porque esta no va a cambiar y tampoco queremos que lo haga.
`fecha_nacimiento = (25, 9, 2005)  `


**Ejercicio 3:**


3. Creación de tuplas
dias_habiles = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
tupla_vacia = ()
un_elemento = ("Python",)
registro = (1052, "Ana Pérez", 8.5)
La coma es la que determina la creación de una tupla; los paréntesis mejoran la legibilidad. 
Por eso una tupla de un único elemento necesita una coma final. 
Verifiquen cada caso con type() y expliquen qué ocurre con type(("Python")) y. type(("Python",))."""


print("Ejemplo 1",type(("Python")))

print("Ejemplo 2 ", type(("Python",)))


**Ejercicio 4:**

a) Mostrar el primer, el último y el elemento central.
productos = ("Teclado", "Mouse", "Monitor", "Auriculares", "Webcam")

print("Primer producto",productos[0])
print("Ultimo producto", productos[4])
print("Producto central ", productos[2])


e) Recorrerla con for e informar cada producto.
productos = ("Teclado", "Mouse", "Monitor", "Auriculares", "Webcam")

for producto in productos:
    print(producto)


**Ejercicio 5:**

a) Informar cantidad, mayor, menor y suma total con len(), max(), min() y sum().

ventas = (120, 85, 230, 150, 90, 150)

print ("Cantidad", len(ventas))
print ("mayor", max(ventas))
print("menor", min (ventas))
print("Suma total", sum(ventas))

**Ejercicio 6:**

Expliquen por qué fecha es una tupla aun sin paréntesis.

Los paréntesis no nos necesarios para la definición de la tupla sino que se utilizan para mejorar la legibilidad, esta queda definida por la separación con comas.


b) Muestren cada variable obtenida mediante desempaquetado.

fecha = dia, mes, anio

print(dia)
print(mes)
print(anio)
