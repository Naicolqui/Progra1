# 1. Concepto y organización de un archivo

Un archivo permite conservar información en un dispositivo no volátil para utilizarla en ejecuciones posteriores del programa. Los archivos pueden clasificarse, entre otros criterios, en **archivos de texto** y **archivos binarios**.

En un archivo de texto los datos se almacenan como caracteres. Cuando se adopta la convención de guardar un registro por línea, el carácter de salto de línea `\n` actúa como delimitador entre registros. Esta organización debe ser definida por el programa: no toda línea de cualquier archivo representa necesariamente un registro.

## Respuestas

### a) ¿Qué significa que la información persista en el tiempo?

La información persiste en el tiempo ya que queda guardada en el archivo para utilizarla en ejecuciones posteriores del programa.

### b) ¿Qué diferencias encuentran entre una variable en memoria y un archivo?

La diferencia entre la variable en memoria y el archivo radica en el tiempo de persistencia de los datos, ya que la información en la variable vive solo durante la ejecución del programa, mientras que el archivo permite conservar esa información.

### c) ¿Qué ventajas y limitaciones presenta almacenar los datos como texto?

**Ventajas:**

- La ya mencionada persistencia de los datos.
- Al ser texto plano, el archivo puede abrirse, leerse y modificarse con cualquier editor de texto (por ejemplo, el Bloc de notas o el IDLE de Python).

**Limitaciones:**

- El acceso es secuencial: se deben leer los registros uno a uno hasta acceder a la información y, al no ser variables en memoria, el acceso puede ser más lento.
- Debe prestarse especial atención a las rutas indicadas para dichos archivos, así como a los permisos sobre las rutas de ubicación.
- Todos los datos se guardan como cadenas de caracteres, por lo que al leerlos hay que convertir los valores numéricos con `int()` o `float()`, y validar que la conversión sea posible.
