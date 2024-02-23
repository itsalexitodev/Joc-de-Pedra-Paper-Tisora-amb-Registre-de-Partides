# -*- coding: utf-8 -*-

import random
import getpass

def registre_jugadors(player1, player2, score, archivo_login):
    try:
        with open(archivo_login, 'w') as f:
            f.write(f'{player1}, {score}\n')
            f.write(f'{player2}, {score}\n')
            game_1vs1(player1, player2)
    except FileNotFoundError:
        print("Archivo no encontrado")  # Mostrar mensaje de error si no se encuentra el archivo

def game_1vs1(player1, playeer2):
    def score():
        return {player1: 0, playeer2: 0}
    score = score()
    pass

def marcador(player1, player2, score):
    # Función para mostrar el puntaje actual
    print("Marcador:")
    print(f"{player1}: {score[player1]}")
    print(f"{player2}: {score[player2]}")

def game_vsCPU(player1):
    pass  # Función provisional para jugar contra la CPU
