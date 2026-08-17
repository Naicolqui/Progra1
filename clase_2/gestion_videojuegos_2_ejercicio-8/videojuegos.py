def mostrar_catalogo(lista):
    obtener_largo = lambda lista: len(lista)
    return lista, obtener_largo

def buscar_juego(lista, titulo):
    for i in range(len(lista)):
        if lista[i] == titulo:
            return i
    return -1

def agregar_juego(lista, titulo):
    if buscar_juego(lista, titulo) == -1:
        lista.append(titulo)
        return True
    return False

def top_n_titulos(lista_inicial):
    # No hace falta un ciclo for para hacer slicing a toda la lista
    cinco_titulos = lista_inicial[0:5]
    tres_ultimos = lista_inicial[-3:]  # Corregido: se usan dos puntos ':' en vez de coma ','
    lista_invertida = lista_inicial[::-1]
    return cinco_titulos, tres_ultimos, lista_invertida

# List Comprehension (> 8 caracteres)
def titulos_8_caracteres(lista):
    return [juego for juego in lista if len(juego) > 8]

