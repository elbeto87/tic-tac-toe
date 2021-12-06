def game_over(board, letter):
    if board[0] == letter:
        if (board[1] == letter and board[2] == letter) or (board[3] == letter and board[6] == letter) or (board[4] == letter and board[8] == letter):
            return True
    if board[1] == letter:
        if board[4] == letter and board[7] == letter:
            return True
    if board[2]:
        if (board[5] == letter and board[8] == letter) or (board[4] == letter and board[6] == letter):
            return True
    if board[3]:
        if (board[4] == letter and board[5]) == letter:
            return True
    if board[6]:
        if board[7] == letter and board[8] == letter:
            return True

def pretty_print(board):
    print("\n")
    print(f"""{board[0]}  |  {board[1]}  |  {board[2]}
{board[3]}  |  {board[4]}  |  {board[5]}
{board[6]}  |  {board[7]}  |  {board[8]}""")
    print("\n")

board_game = ['_','_','_','_','_','_','_','_','_']
player_1 = ['X', 'X', 'X', 'X', 'X']
player_2 = ['O', 'O', 'O', 'O', 'O']

while ('X' in player_1) and ('O' in player_2):
    print("Por favor, ingrese una posición player_1: ")
    value = int(input())
    board_game[value-1] = 'X'
    pretty_print(board_game)
    player_1.pop()
    if (game_over(board_game, board_game[value-1])):
        print("Player_1 ha ganado! Felicitaciones")
        break
    else:
        if ('X' in player_1) and ('O' in player_2):
            print("Por favor, ingrese una posición player_2: ")
            value = int(input())
            board_game[value-1] = 'O'
            pretty_print(board_game)
            player_2.pop()
            if (game_over(board_game, board_game[value-1])):
                print("Player_2 ha ganado! Felicitaciones")
                break
else:
    print("Empate!")
    pretty_print(board_game)





