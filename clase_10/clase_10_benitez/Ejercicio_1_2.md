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



# 2. Apertura, procesamiento y cierre
Todo trabajo con archivos comprende tres momentos: apertura, procesamiento y cierre. El modo utilizado al abrir el
archivo determina qué operaciones pueden realizarse.
Analicen los modos más frecuentes:
a) "rt": lectura; el archivo debe existir.
b) "wt": escritura; crea el archivo o reemplaza todo su contenido si ya existe.
c) "at": agregado; crea el archivo o escribe al final sin borrar lo anterior.
with open("notas.txt", "wt", encoding="utf-8") as archivo:
archivo.write("Primer registro\n")
archivo.write("Segundo registro\n")
archivo.write("Tercer registro\n")
Expliquen qué función cumplen open(), write() y la estructura with. Observen que write() recibe una cadena y que el salto de línea debe incorporarse expresamente. with cierra el archivo aun cuando se produzca una  excepción dentro del bloque.



### Open (): 
Apertura del archivo, devuelve un objeto archivo sobre el que se trabaja a lo largo del código.
Recibela ruta, el modo y la codificación del archivo.

### Write ():
escribe exactamente la cadena que recibe, en la posición actual del archivo.
-Solo acepta cadenas: archivo.write(5) da TypeError: write() argument must be str, not int. 
Para escribir un número hay que convertirlo antes con str()

-No agrega el salto de línea: Si se escribe "Primer registro" y "Segundo registro" sin \n, el archivo queda Primer registroSegundo registro, todo en una línea. Por eso cada registro termina en "\n". Con el código del ejemplo, el archivo queda con tres líneas.




### With ():
cierra automáticamente  el archivo al salir, sin necesidad de llamar a close(). Lo cierra tanto si el bloque termina normalmente como si ocurre una excepción.

Si no se utilizara With, de ocurrir alguna excepción no capturada antes de la linea de donde se llama a close (), esta linea no se ejecuta y el archivo quedaría abierto.

