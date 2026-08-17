# Desafío integrador
# Desarrollen un pequeño sistema de gestión de videojuegos dividido en los módulos videojuegos.py y principal.py. 
# El programa deberá:
# • Crear una lista inicial con diez títulos. (1)
# • Mostrar el catálogo y su cantidad de elementos. (1)
# • Buscar un título ingresado por el usuario. (2)
# • Agregarlo únicamente cuando no se encuentre repetido. (3)
# • Mostrar los primeros cinco títulos, los tres últimos y el catálogo invertido mediante slicing.(4)
# • Crear por comprensión una nueva lista con los títulos cuya longitud sea mayor que ocho caracteres.(5)
# • Utilizar al menos una función lambda de la sección anterior.
# • Mantener en principal.py la entrada y salida general, y en videojuegos.py las operaciones del catálogo.

#programa
import videojuegos

juegos = [
    "Minecraft", "Valorant", "Fortnite", "Grand Theft Auto V",
    "Tetris", "FIFA 24", "Counter Strike", "League of Legends",
    "Zelda", "Pac-Man"
]

# 1. Mostrar catálogo
lista,obtener_largo = videojuegos.mostrar_catalogo(juegos)
print(f"Cantidad de elementos en el catálogo: {obtener_largo(juegos)}")
print(f"Catálogo inicial: {lista}")


#2
print(f"Resultado de la búsqueda, esta en la posición (si devuelve -1, no está): {videojuegos.buscar_juego(juegos, 'FIFA 24')}")

#3
print(f"Agregando un juego nuevo, si devuelve True se agregó, si devuelve False ya estaba: {videojuegos.agregar_juego(juegos, 'Among Us')}")

#4
cinco, tres, invertida = videojuegos.top_n_titulos(juegos)
print("\nPrimeros 5:", cinco)
print("Últimos 3:", tres)
print("Invertidos:", invertida)

#5
largos = videojuegos.titulos_8_caracteres(juegos)
print("\nTítulos con más de 8 caracteres:")
print(largos)

