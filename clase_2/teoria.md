1. Repaso de la clase anterior
Antes de comenzar, respondan en grupo:
a) ¿Qué diferencia existe entre problema, algoritmo y programa?
Problema: es aquello que necesita solución. Ej: necesito calcular el promedio de ventas de una empresa por día.
Algoritmo: Es el paso a paso de como se va a resolver cada problema.
Programa: Es la implementación del algoritmo de forma que se puede ejecutar en un lenguaje de programación específico.
b) ¿Qué ventaja ofrece dividir un programa en funciones?
Se puede reutilizar el código en varios lugares sin tener que repetirlo cada vez que necesitamos usarlo.
Es mas facil de leer y de mantener. Es decir, reduce la complejidad.
c) ¿Qué diferencia existe entre mostrar un resultado y retornarlo?
Mostrar el resultado implica mostrarlo en consola pero el dato no puede ser usado, solo visualizado.
Cuando se retorna un valor la función termina y el valor puede ser usado para alguna otra aplicación.
d) ¿Cómo se accede, modifica y recorre una lista?
Para acceder a una lista debo recorrerlo a partir del indice donde esta el valor.
Ejemplo:
lista = [1,2,3]
print(lista[2]) me va a imprimir el 3.
Segun la información de la clase nueva también se puede utilizar el slicing.

Para modificar una lista podemos:
- Cambiarlo: lista[0] = 4 --> ahora la lista va a ser [4,2,3]
- Agregarle un elemento: lista.append(2) --> ahora la lista va a ser [4,2,3,2]
- Eliminar: 
    - lista.pop(1) --> elimina el valor en la posicion 1 que en este caso sería 2
    - lista.remove(2) --> va a eliminar el primer valor que coincida
    - segun la nueva clase se puede utilizar el slicing también para cambiar valores en indices determinados.

1-4-7
