# 3. Análisis y construcción de patrones

Indiquen qué formato representa cada expresión y propongan dos datos válidos y dos inválidos:

`r”^PROG[0-9]{3}$”`

Representa: Cadena “PROG” seguida de 3 caracteres en el rango de 0 a 9.

Ejemplo valido: PROG000, PROG111

Ejemplo invalido: 999PROG, PROG23456

---

`r”^[A-Za-z]{3,10}$”`

Representa: Cadena de caracteres, solo letras, de entre 3 y 10 caracteres, pudiendo ser minúsculas y mayusculas.

Ejemplo valido: Ana, Xilofon

Ejemplo invalido: La gata se llama Lana, Prueba123

---

`r”^[0-9]{4}-[0-9]{4}$"` 0000 - 0000

Representa: Patron de 4 dígitos- 4 dígitos

Ejemplo valido: 1000-1562, 2012-2020

Ejemplo invalido: 192930-a1930, 8827-AAAAA

---

`r”^([A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2})$”`

Representa: 3 letras mayúsculas 3 numeroso o 2 letras mayusculas, 3 digitos, 2 mayusculas nuevamente

Ejemplo valido: ABC111, AB111CD

Ejemplo invalido: 111ABC, AB111CDEF

---

## Patrones para validar:

a) Un código formado por dos letras mayúsculas y cuatro números.

Patron:

`r”^[A-Z]{2}[0-9]{4}$”`

b) Un legajo de exactamente cinco dígitos.

`r”^[A-Za-z0-9]{5}$”`

c) Un importe formado por el símbolo $ y uno o más dígitos. Recuerden escapar el símbolo: `\$`.

`r"^\$[0-9]+$"`

d) Una palabra que comience con mayúscula y continúe únicamente con letras.

e) Una fecha con formato DD/MM/AAAA, validando solamente la forma y no la existencia real de la fecha.

`r”^[0-9]{2}/[0-9]{2}/[0-9]{4}$"`

---

Los patrones con `[A-Za-z]` no contemplan letras acentuadas ni ñ. Documenten el alcance de cada validación y no confundan una validación de formato con una validación semántica del dato.

Esta validación cubre ejemplos como el brindado, Ana, pero excluye ejemplos como Iñaki, o Nicolás que son ejemplos validos si lo que necesitamos validar es el ingreso de una cadena de caracteres que represe nombre.
Semánticamente es correcto pero no cumplen con la validación de formato aplicada.

# 6. sub, split y compile


d) Explicar cuándo mejora la legibilidad compilar una expresión regular.

```python
patron_anio = re.compile(r"[0-9]{4}")
fechas = "07/08/2017|03/02/1984|17/03/2001"
anios = patron_anio.findall(fechas)
```



La principal ventaja de compilar una expresión regular es que permite optimizar las búsquedas, especialmente cuando la misma expresión se utiliza varias veces en el código. Además, al compilarla, se mejora tanto la legibilidad como el rendimiento del programa, ya que se evita tener que recompilar la misma expresión en cada uso. Una vez compilada, la expresión se convierte en un objeto que puede utilizarse para invocar los métodos vistos anteriormente, de forma similar a como se haría directamente con el módulo re.

# 9.Comparación entre búsqueda parcial y validación completa.

La búsqueda parcial, que realizan match(), search() y findall(), verifica si el patrón aparece en alguna punto de la cadena: match() lo busca al inicio y search() y findall() en cualquier posición, antes o después en la cadena.
Para  la validación completa con fullmatch(), se exige que el patrón coincida con la cadena completa.
Es por esto que  la búsqueda parcial resulta útil para encontrar o extraer información dentro de un texto más largo, y la validación completa e para comprobar que un dato ingresado en un formulario cumpla exactamente con el formato definido.