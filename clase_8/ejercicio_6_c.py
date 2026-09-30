
import re

texto = "351-482-7710 Hola, soy Laura. ¿Me llamás al 351-482-7710 o al 11-4567-8901? Mi oficina atiende en el 223-915-3348 desde 2019. Otro número viejo: 3514827710"
cadena= "XXX-XXX-XXXX"
patron_telefono = re.compile(r"[0-9]{3}-[0-9]{3}-[0-9]{4}")

print("Busqueda con findall:", patron_telefono.findall(texto))
print("Reemplazo con sub:", patron_telefono.sub(cadena, texto))
match=patron_telefono.match(texto)
if match:
    print("Se encontraron coincidencias al INICIO de la cadena")
    print(patron_telefono.match(texto))
else:
    print("No se encontraron coincidencias AL INICIO de la cadena")




