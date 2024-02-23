# -*- coding: utf-8 -*-

from juego import *

def main():
    print("\n Bienvenido al Juego del Piedra, Papel, Tijeras")
    
    while True:
        print("\nQue quieres hacer?\n")
        print("1. 1vs1")
        print("2. VS CPU ")
        print("3. Salir\n")
        print("Seleccione una opcion (1 - 3):\n")
        opcion = input()

        if opcion == "1":
            print("Ingrese el nombre del jugador 1:")
            player1 = input()
            
            print("Ingrese el nombre del jugador 2:")
            player2 = input()
            registre_jugadors(player1, player2)
        elif opcion == "2":
            print("Ingrese su nombre:")
            player1 = input()
            game_vsCPU(player1)
        elif opcion == "3":
            print("Gracias por jugar!")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del (1 - 3).")

if __name__ == "__main__":
    main()
