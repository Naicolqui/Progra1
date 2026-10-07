""" 9. Actividad integradora: análisis de una frase
Desarrollar un programa que solicite una frase y realice las siguientes tareas:
a) Normalizarla a minúsculas.
b) Eliminar, como mínimo, punto, coma, punto y coma, dos puntos, signos de pregunta y exclamación.
c) Separarla en palabras.
d) Crear un conjunto con las palabras diferentes.
e) Crear un diccionario de frecuencias donde cada palabra sea una clave y su cantidad de apariciones sea el valor.
f) Mostrar las palabras sin repetir en orden alfabético.
g) Mostrar cada palabra con su frecuencia.
h) Informar la palabra más frecuente solo si se ingresó al menos una palabra.
frecuencias = {}
for palabra in palabras:
 frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
Prueben con una frase que contenga palabras repetidas, diferencias de mayúsculas y signos de puntuación. Incluyan 
también una cadena vacía o formada solo por espacios para evitar aplicar max() a un diccionario vacío """

def main():
    frase = input("Ingrese una frase: ")

    frase = frase.lower()

    for signo in [".", ",", ";", ":", "?", "!", "¿", "¡"]:
        frase = frase.replace(signo, "")

    palabras = frase.split()

    unicas = set(palabras)

    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    print("Palabras sin repetir:", sorted(unicas))

    for palabra in sorted(frecuencias):
        print(palabra, "->", frecuencias[palabra])

    if len(frecuencias) > 0:
        mas_frecuente = max(frecuencias, key=frecuencias.get)
        print("Palabra mas frecuente:", mas_frecuente, "(", frecuencias[mas_frecuente], "veces )")
    else:
        print("No se ingresaron palabras.")

if __name__ == "__main__":
    main()

