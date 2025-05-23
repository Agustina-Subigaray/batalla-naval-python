import random

def crear_tablero():
    columnas = ["A", "B", "C", "D", "E"]
    filas = [1, 2, 3, 4, 5]
    tablero = {}
    for fila in filas:
        tablero[fila] = {}
        for col in columnas:
            tablero[fila][col] = " "
    return tablero

def colocar_naves(tablero, cantidad=3):
    colocadas = 0
    while colocadas < cantidad:
        fila = random.randint(1, 5)
        col = random.choice(["A", "B", "C", "D", "E"])
        if tablero[fila][col] == " ":
            tablero[fila][col] = "N"
            colocadas += 1

def mostrar_tablero(tablero, ocultar_naves=True):
    print("  A B C D E")
    for fila in range(1, 6):
        fila_str = f"{fila} "
        for col in ["A", "B", "C", "D", "E"]:
            celda = tablero[fila][col]
            if ocultar_naves and celda == "N":
                fila_str += "· "
            else:
                fila_str += f"{celda} "
        print(fila_str)

def jugar():
    mio = crear_tablero()
    enemigo = crear_tablero()
    mio_tiro = crear_tablero()
    enemigo_tiro = crear_tablero()

    colocar_naves(mio)
    colocar_naves(enemigo)

    while True:
        print("\n--- MENÚ ---")
        print("1. Ver mi mapa")
        print("2. Ver mis tiros")
        print("3. Disparar al enemigo")
        print("4. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            print("🗺 Tu mapa:")
            mostrar_tablero(mio, ocultar_naves=False)
        elif opcion == "2":
            print("🎯 Tus tiros:")
            mostrar_tablero(mio_tiro, ocultar_naves=False)
        elif opcion == "3":
            coord = input("Ingresá coordenada (ej. A3): ").upper()
            if len(coord) >= 2 and coord[0] in "ABCDE" and coord[1] in "12345":
                col = coord[0]
                fila = int(coord[1])
                if enemigo[fila][col] == "N":
                    print("💥 ¡Le diste!")
                    enemigo[fila][col] = "X"
                    mio_tiro[fila][col] = "X"
                elif enemigo[fila][col] == " ":
                    print("💧 Agua.")
                    enemigo[fila][col] = "-"
                    mio_tiro[fila][col] = "-"
                else:
                    print("Ya disparaste ahí.")
            else:
                print("Coordenada inválida.")
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida.")

# Ejecutar el juego
jugar()
