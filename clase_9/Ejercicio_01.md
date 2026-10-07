# 1. Primer contacto con los conjuntos

```python
lenguajes = {"Python", "Java", "C", "Python", "C"}
vacio = set()
print(lenguajes)
print(type(vacio))
```

Ejecuten el código y respondan:

**a) ¿Por qué los valores repetidos aparecen una sola vez?**

Los elementos repetidos del conjunto, al imprimirlos aparecen solo una vez ya que la estructura no lo permite al trabajar como conjuntos matemáticos, donde un elemento pertenece o no a un conjunto.

**b) ¿Por qué un conjunto vacío se crea con `set()` y no con `{}`?**

Se crea con `set()` de forma de poder diferenciarlo de un diccionario vacío.
Cuando ambas estructuras tienen elementos es distinguible: `{1, 2}` es un conjunto y `{1: "a"}` es un diccionario, pero de otra forma Phyton no tiene como distinguirlo.

**c) ¿Sería correcto intentar mostrar `lenguajes[0]`? Justifiquen.**

No seria correcto, ya que los elementos no respetan un orden especifico dentro del conjunto.
En las sucesivas pruebas, al imprimirlo el orden de lenguajes se muestra distinto, porque los conjuntos no admiten acceso por índice.