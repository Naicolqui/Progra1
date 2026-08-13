def main():
    juegos = ["Minecraft", "Valorant", "Fortnite", "FIFA",
     "Rocket League", "Roblox", "LOL", "Among Us"]

    print(juegos[0:3]) ##Obtengo los 3 primeros elementos
    print(juegos[4:]) ## Obtengo los ultimos 4 elementos
    print(juegos[1:5]) ##Los elementos ubicados desde la posición 1 hasta la 4 inclusive.
    print(juegos[::2]) ## Los elementos de posiciones pares.
    print(juegos[1::2]) ## Los elementos de posiciones impares.
    print(juegos[::-1]) ## La lista invertida.
    print(juegos[1:]) ## Todos los elementos excepto el primero.
    print(juegos[0:7]) ## Todos los elementos excepto el último.


if __name__ == "__main__":
    main()
