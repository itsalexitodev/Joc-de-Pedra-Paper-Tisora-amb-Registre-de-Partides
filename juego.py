def mostrar_marcador(player1, player1_stats, player2, player2_stats):
    print("\nMarcador:\n")
    print(f"{player1}: {player1_stats['ganadas']} ganadas, {player1_stats['perdidas']} perdidas")
    print(f"{player2}: {player2_stats['ganadas']} ganadas, {player2_stats['perdidas']} perdidas")

def ganador(opcion, empate):
    if opcion == empate:
        return "Empate"
    elif (opcion == "piedra" and empate == "tijeras") or (opcion == "papel" and empate == "piedra") or (opcion == "tijeras" and empate == "papel"):
        return "Jugador 1"
    else:
        return "Jugador 2"

def opciones(player1, player2):
    opciones = ["piedra", "papel", "tijeras"]
    player1_opcion = input(f"{player1}, elige entre piedra, papel o tijeras: ").lower()
    player2_opcion = input(f"{player2}, elige entre piedra, papel o tijeras: ").lower()
    if player1_opcion not in opciones or player2_opcion not in opciones:
        print("Opción inválida, por favor elige entre piedra, papel o tijeras.")
        return opciones(player1, player2)
    return player1_opcion, player2_opcion

def game_1vs1(players, player1, player2):
    print(f"\n¡Comienza el juego entre {player1} y {player2}!\n")
    while True:
        player1_opcion, player2_opcion = opciones(player1, player2)
        print(f"\n{player1} eligió {player1_opcion}.")
        print(f"{player2} eligió {player2_opcion}.\n")
        resultado = ganador(player1_opcion, player2_opcion)
        print(f"Resultado: {resultado}\n")
        if resultado == "Jugador 1":
            players[player1]['ganadas'] += 1
            players[player2]['perdidas'] += 1
        elif resultado == "Jugador 2":
            players[player2]['ganadas'] += 1
            players[player1]['perdidas'] += 1
        else:
            print("Empate.")
        mostrar_marcador(player1, players[player1], player2, players[player2])
        continuar = input("\n¿Quieres jugar otra ronda? (s/n): ")
        if continuar.lower() != 's':
            break
    return players

def game_vsCPU(players, player1):
    print(f"\n¡Comienza el juego contra la CPU, {player1}!\n")
    while True:
        player1_opcion = input(f"{player1}, elige entre piedra, papel o tijeras: ").lower()
        cpu_opcion = random.choice(["piedra", "papel", "tijeras"])
        print(f"La CPU eligió {cpu_opcion}.\n")
        resultado = ganador(player1_opcion, cpu_opcion)
        print(f"Resultado: {resultado}\n")
        if resultado == "Jugador 1":
            players[player1]['ganadas'] += 1
        elif resultado == "Jugador 2":
            players[player1]['perdidas'] += 1
        else:
            print("Empate.")
        print(f"Marcador: {players[player1]['ganadas']} ganadas, {players[player1]['perdidas']} perdidas\n")
        continuar = input("¿Quieres jugar otra ronda? (s/n): ")
        if continuar.lower() != 's':
            break
