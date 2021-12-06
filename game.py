def presentation():
    board_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    player_1 = input("Por favor, ingrese el nombre del primer jugador: ")
    player_2 = input("Por favor, ingrese el nombre del segundo jugador: ")
    print(f"\nBienvenidos al juego {player_1.capitalize()} y {player_2.capitalize()}\n")
    print("""Para elegir donde quieren poner su ficha, van a tener la siguiente disposición numérica
      1   |   2   |   3   
      4   |   5   |   6   
      7   |   8   |   9   
      
    """)
    play_game(player_1, player_2)

def game_over(board, letter):
    if board[0] == letter:
        if (board[1] == letter and board[2] == letter) or (board[3] == letter and board[6] == letter) or (board[4] == letter and board[8] == letter):
            return True
    if board[1] == letter:
        if board[4] == letter and board[7] == letter:
            return True
    if board[2] == letter:
        if (board[5] == letter and board[8] == letter) or (board[4] == letter and board[6] == letter):
            return True
    if board[3] == letter:
        if (board[4] == letter and board[5]) == letter:
            return True
    if board[6] == letter\
            :
        if board[7] == letter and board[8] == letter:
            return True


def pretty_print(board):
    print("\n")
    print(f"""{board[0]}  |  {board[1]}  |  {board[2]}
{board[3]}  |  {board[4]}  |  {board[5]}
{board[6]}  |  {board[7]}  |  {board[8]}""")
    print("\n")


def play_game (player1, player2):

    board_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    player1_chips = ['X', 'X', 'X', 'X', 'X']
    player2_chips = ['O', 'O', 'O', 'O', 'O']

    while ('X' in player1_chips) and ('O' in player2_chips):
        value = input_value(player1, board_game)
        board_game[value - 1] = 'X'
        pretty_print(board_game)
        player1_chips.pop()
        if (game_over(board_game, 'X')):
            print(f"{player1.capitalize()} ha ganado! Felicitaciones")
            break
        else:
            if ('X' in player1_chips) and ('O' in player2_chips):
                value = input_value(player2, board_game)
                board_game[value-1] = 'O'
                pretty_print(board_game)
                player2_chips.pop()
                if (game_over(board_game, 'O')):
                    print(f"{player2.capitalize()} ha ganado! Felicitaciones")
                    break
    else:
        print(f"Empate! entre {player1.capitalize()} y {player2.capitalize()}")
        pretty_print(board_game)

def input_value(player, board):
    print(f"Por favor, ingrese una posición {player}:")
    value_position = int(input())
    while board[value_position - 1] != '_':
        value_position = int(input("El casillero está ocupado, por favor, ingrese un valor válido"))
    return value_position


presentation()



