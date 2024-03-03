from juego import *

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    player1 = input("Nombre del jugador 1: ")
    player2 = input("Nombre del jugador 2: ")
    players = {player1: {'ganadas': 0, 'perdidas': 0},
               player2: {'ganadas': 0, 'perdidas': 0}}
    mostrar_marcador(player1, players[player1], player2, players[player2])
    print("\nSelecciona el modo de juego:\n")
    print("1. Jugar contra otro jugador")
    print("2. Jugar contra la CPU")
    modo_juego = input("\nIngresa el número del modo de juego: \n")
    if modo_juego == '1':
        game_1vs1(players, player1, player2)
    elif modo_juego == '2':
        game_vsCPU(player1)
    else:
        print("Modo de juego no válido. Por favor selecciona 1 o 2.")

if __name__ == "__main__":
    main()
