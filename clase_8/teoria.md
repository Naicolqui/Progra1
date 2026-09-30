## Cualquier cosa != 0 es verdadero
## None es falso

a) ¿Qué diferencia existe entre un patrón literal y uno que contiene metacaracteres?
Un patron literal se representa a si mismo, mientras que un metacaracter es interpretado de una forma diferente. A traves de los metacaracteres podemos definir diferentes condiciones tales como agrupaciones, alternativas, comodines, multiplicadores y demás.
b) ¿Qué significa encontrar una coincidencia o match?
Significa hayar un valor dentro de una cadena de texto de coincide con el patron previamente dado por la expresión regular.
c) ¿Para qué se utiliza el módulo re de Python?
Lo utilizamos para para trabajar con expresiones regulares. Basicamente nos provee todas las herramientas necesarias para realizar operaciones avanzadas de busqueda de estos patrones dentrod de determinadas cadenas de texto.
d) ¿Por qué conviene escribir los patrones como cadenas crudas, por ejemplo r"[0-9]+"?
Conviene escribirlos como cadenas crudas (raw strings, con el prefijo r) porque tanto las expresiones regulares como Python usan la barra invertida (\) como caracter especial, pero con significados distintos. Si escribimos un patron como "\n" en una cadena normal, Python lo interpreta como un salto de linea antes de que llegue al modulo re. En cambio, secuencias propias de las regex como \d, \w o \b no significan nada para Python, asi que sin el prefijo r corremos el riesgo de errores o comportamientos inesperados. Al usar r"..." le decimos a Python que no interprete las barras invertidas, dejando que sea el modulo re quien las procese correctamente segun la sintaxis de expresiones regulares.


REFLEXION

Las expresiones regulares permiten buscar y extraer información de textos de forma rápida y eficiente, especialmente cuando los datos siguen un patrón. Sin embargo, pueden resultar difíciles de leer y mantener cuando los patrones son muy largos o complejos, por lo que es importante escribirlos de manera clara y comentada.
