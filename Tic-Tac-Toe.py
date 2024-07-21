def nextMove(player, board):
    player_char = player
    opponent_char = 'O' if player_char == 'X' else 'X'

    # Function to check if a player has won
    def is_winner(board, player):
        # Check elements in row
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
        # Check column elements
        for j in range(3):
            if all(board[i][j] == player for i in range(3)):
                return True
        # Check diagonals
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False

    # Function to find a winning move
    def find_winning_move(board, player):
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    if is_winner(board, player):
                        board[i][j] = '_'
                        return (i, j)
                    board[i][j] = '_'
        return None

    # Function to find the best available move
    def find_best_move(board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    return (i, j)
        return None

    # Check if there is a winning move
    move = find_winning_move(board, player_char)
    if move is not None:
        print(move[0], move[1])
        return

    # blocking move
    move = find_winning_move(board, opponent_char)
    if move is not None:
        print(move[0], move[1])
        return

    move = find_best_move(board)
    if move is not None:
        print(move[0], move[1])
        return

# Read input
player = input().strip()
board = [list(input().strip()) for _ in range(3)]

nextMove(player, board)
