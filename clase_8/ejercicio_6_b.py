
import re

#b) Utilizar re.split() para dividir un texto usando puntos, comas, signos de pregunta y espacios como separadores.

texto="Hola, soy Laura. ¿Me llamás al 351-482-7710 o al 11-4567-8901?  Mi oficina atiende en el 223-915-3348 desde 2019. Otro número viejo: 3514827710 "

patron=  r"[.,? ]+"

division=re.split(patron,texto)

print(division)











