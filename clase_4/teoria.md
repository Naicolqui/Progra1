**Ejercicio 1:**

¿Qué significa que un objeto sea mutable o inmutable?

Un objeto es mutable cuando se puede modificar su contenido después de haberlo creado, sin necesidad de generar uno nuevo. A diferencia de un objeto inmutable, el cual una vez creado no se puede alterar.

**Ejercicio 2:**
a)Ambos son secuencias ordenadas de elementos.Se puede acceder a sus elementos mediante índices (ej. elemento[0]) y slicing/rebanadas ([1:3]).Pueden contener elementos de distintos tipos de datos (enteros, texto, float, etc.)Ambas se pueden recorrer con un bucle for y consultar su tamaño con len().
b)Inmutabilidad: Las listas son mutables (se pueden modificar, agregar o eliminar elementos mediante .append(), .pop(), etc.), mientras que las tuplas son inmutables (su tamaño y contenido fijo no se pueden cambiar una vez creadas).
Sintaxis: Las listas usan corchetes [1, 2, 3] y las tuplas usan paréntesis (1, 2, 3).
c) Da el siguiente error : 
TypeError: 'tuple' object does not support item assignment

Esto confirma que las tuplas son inmutables y no permiten modificar sus elementos una vez creadas.

![Comprobación del TypeError](Comprobacion-tuplas.png)


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

c) 
# Intento de desempaquetado en dos variables:
dia_nac, mes_nac = fecha

Al ejecutar dia_nac, mes_nac = fecha, Python arroja el error:
ValueError: too many values to unpack (expected 2)

Esto ocurre porque la tupla fecha contiene 3 elementos (25, "Septiembre", 2026), pero en la asignación solo se le están pasando 2 variables (dia_nac y mes_nac). Python no puede determinar por sí solo cuál de los tres datos ignorar, por lo que detiene el programa.

d)Para que el desempaquetado funcione correctamente, debe cumplirse una relación exacta 1 a 1: la cantidad de variables a la izquierda del signo = debe ser estrictamente igual a la cantidad de elementos contenidos en la tupla. 




**Reflexion :**

Usaríamos una lista al trabajar con  una colección homogénea que va a crecer, achicarse o reordenarse. En cambio el uso de una tupla resultaría mejor al trabajar con conjuntos fijo de valores relacionados y se necesite la inmutabilidad garantizada de dichos datos


