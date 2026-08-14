# 1. Repaso de la clase anterior

Antes de comenzar, respondan en grupo:

### a) ¿Qué diferencia existe entre problema, algoritmo y programa?

- **Problema**: es aquello que necesita solución. Ej: necesito calcular el promedio de ventas de una empresa por día.
- **Algoritmo**: es el paso a paso de cómo se va a resolver cada problema.
- **Programa**: es la implementación del algoritmo de forma que se pueda ejecutar en un lenguaje de programación específico.

### b) ¿Qué ventaja ofrece dividir un programa en funciones?

- Se puede reutilizar el código en varios lugares sin tener que repetirlo cada vez que necesitamos usarlo.
- Es más fácil de leer y de mantener. Es decir, reduce la complejidad.

### c) ¿Qué diferencia existe entre mostrar un resultado y retornarlo?

- **Mostrar** el resultado implica mostrarlo en consola, pero el dato no puede ser usado, solo visualizado.
- Cuando se **retorna** un valor, la función termina y el valor puede ser usado para alguna otra aplicación.

### d) ¿Cómo se accede, modifica y recorre una lista?

Para acceder a una lista debo recorrerla a partir del índice donde está el valor.

Ejemplo:

```python
lista = [1, 2, 3]
print(lista[2])  # imprime el 3
```

Según la información de la clase nueva, también se puede utilizar el slicing.

Para modificar una lista podemos:

- **Cambiar un valor**: `lista[0] = 4` → ahora la lista va a ser `[4, 2, 3]`
- **Agregar un elemento**: `lista.append(2)` → ahora la lista va a ser `[4, 2, 3, 2]`
- **Eliminar**:
  - `lista.pop(1)` → elimina el valor en la posición 1 (en este caso sería 2)
  - `lista.remove(2)` → elimina el primer valor que coincida
  - Según la nueva clase, también se puede utilizar el slicing para cambiar valores en índices determinados.
 



#3.Funciones que reciben listas
Antes de programar, clasifiquen cada función del punto anterior según corresponda: retorna un valor, modifica la lista recibida o solamente muestra información.
Funciones ejercicio anterior:

* mostrar_juegos() solamente muestra información
* buscar_juego() retorna la posición
* agregar_juego() modifica la lista
* cantidad_juegos() retorna valor

Luego realicen pruebas con una lista de diez videojuegos y respondan:
###a)¿Qué contenido tiene la lista antes y después de llamar a agregar_juego()?

El contenido inicial de la lista es: 
juegos = ["Minecraft", "Valorant", “Fortnite”]

Luego llamar agregar_juego() tendremos la lista juegos con el agregado de los nuevos juegos:

juegos = ["Minecraft", "Valorant", “Fortnite”,”juego4”,”juego5”,”juego6”,”juego7”,”juego8”,”juego9”,”juego10”]


###b) ¿Qué retorna buscar_juego() cuando el título existe? ¿Y cuando no existe?

Cuando el titulo existe devuelve la posición del juego en la lista, en caso de no existir, devuelve -1

###c) ¿Por qué una función puede modificar una lista recibida como parámetro?

Una función puede modificar una lista si ésta es enviada como parámetro ya que se envía la posición de memoria de la lista original, y la función trabaja sobre ello.
En caso de requerir no modificar la lista original, se puede generar una copia de la misma.


###d) ¿Qué datos conviene solicitar en principal.py y cuáles debe procesar el módulo?

En principal: lista de de juegos, nombre del videojuego a buscar, a mostrar o a agregar

En el modulo: entregarle los datos solicitados para trabajarlos por parámetro.
