""""6. Funciones y métodos de cadenas
Recuerden que los métodos que transforman una cadena retornan una nueva cadena; no modifican el objeto original. 
Prueben y registren el resultado de cada operación.
a) texto.upper()
b) texto.lower()
c) texto.title()
d) texto.capitalize()
e) texto.replace("Python", "IA")
f) texto.count("a")
g) texto.find("Python")
h) len(texto)
Analicen además los métodos de validación con las cadenas "Programacion", "2026", "Python3" y "Programacion en 
Python": isalpha(), isdigit() e isalnum(). Expliquen por qué isalpha() retorna False cuando la cadena contiene espacios, 
aunque todas sus palabras estén formadas por letras.
"""


texto = "Programacion en Python"

print("UPPER:",texto.upper())
print("LOWER:",texto.lower())
print("TITLE:", texto.title())
print("CAPITALIZE:",texto.capitalize())
reemplazo= texto.replace('Phyton','IA')
print("Reemplazo: ", reemplazo)
print("Cantidad de a: ",texto.count("a"))
print("Posicion donde Encontro:", texto.find("Python"))
print("Largo de la candena: ", len(texto))







"""Analicen además los métodos de validación con las cadenas "Programacion", "2026", "Python3" y "Programacion en 
Python": isalpha(), isdigit() e isalnum(). Expliquen por qué isalpha() retorna False cuando la cadena contiene espacios, 
aunque todas sus palabras estén formadas por letras.



* Metodos de validacion que preguntan por el tipo de contenido de una cadena
isalpha() = consulta si es texto, ejemplo:  "Programacion", "Programacion en 
Python"

isdigit() = consulta si en son solo numeros, ejemplo: "2026"
isalnum() = consulta si es alfanumerico, ejemplo: "Python3"
isalnum() retornara False cuando contenga espacios ya que este no se considera como un caracter alfanumerico.


