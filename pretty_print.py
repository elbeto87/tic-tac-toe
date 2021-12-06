board_game = ['X','O','X','_','O','_','O','_','_']

def pretty_print(board):
    print(f"""__{board[0]}__  |  __{board[1]}__  |  __{board[2]}__
__{board[3]}__  |  __{board[4]}__  |  __{board[5]}__
__{board[6]}__  |  __{board[7]}__  |  __{board[8]}__""")

pretty_print(board_game)
