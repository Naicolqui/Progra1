# Git, GitHub y cadenas de caracteres
# Orientador Clase 3

# 1. Repaso de la clase anterior 
# Antes de comenzar, respondan en grupo: 
a) ¿Qué ventajas ofrece separar un programa en módulos?
Hace más fácil la lectura y el mantenimiento del código, evita duplicar líneas, permite reutilizar funciones en diferentes partes del proyecto y facilita la detección de errores.

b) ¿Qué diferencia existe entre una lista y una cadena de caracteres?
Una lista es una colección ordenada y mutable de elementos de cualquier tipo (números, textos, etc.), mientras que una cadena de caracteres (string) es una secuencia inmutable formada únicamente por caracteres.

c) ¿Qué significa que un dato sea mutable o inmutable?
Un dato mutable (como las listas) permite modificar, agregar o eliminar su contenido después de ser creado. Un dato inmutable (como los strings o tuplas) no puede cambiar su valor original una vez definido.

d) ¿Qué responsabilidades conviene dejar en el programa principal y cuáles en las funciones?
El programa principal debe encargarse del flujo general, la interacción con el usuario (pedir entradas con input y mostrar resultados con print) y las llamadas a funciones. Las funciones deben asumir el procesamiento de datos, los cálculos y la lógica del negocio de manera aislada.


# Git y GitHub

Git es un sistema de control de versiones que registra cambios en los archivos de un proyecto. GitHub es un servicio que permite alojar repositorios remotos y facilitar el trabajo colaborativo. No son la misma herramienta: Git administra versiones; GitHub permite compartirlas y coordinarlas.


# 2.Relacionen cada concepto con su función:

- **a) Repositorio local**: Es el proyecto guardado en nuestra máquina, con la última versión disponible en la misma.
- **b) Repositorio remoto**: Es el proyecto guardado en un servidor remoto, en este caso GitHub, con sus respectivas versiones que hayan sido subidas por los distintos colaboradores.
- **c) Área de preparación o staging**: Es el espacio intermedio donde se seleccionan los cambios que se desean incluir en el próximo commit, antes de ser confirmados en el repositorio local.
- **d) Commit**: Es un registro que guarda los cambios realizados en los archivos, acompañado de un mensaje descriptivo que explica qué se modificó y por qué (idealmente). Representa una versión del estado del proyecto en un momento específico.
- **e) Push y pull**: push es un comando a través del cual publicamos los commits que hicimos de forma local en nuestro repositorio, de forma que pasa a ser remoto. Con pull nos traemos a nuestro repo local la última versión disponible en el repositorio remoto.

La actividad integradora mencionada en el punto 8 del orientador de la clase va a ser llevada a cabo dentro del proyecto integrador y su respectivo repositorio: [https://github.com/jessbenitez/ProyectoProgramacionI](https://github.com/jessbenitez/ProyectoProgramacionI)