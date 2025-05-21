board = [' ' for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def play_game():
    current = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current}, choose (0-8): "))
        
        if board[move] != ' ':
            print("That spot is taken. Try again.")
            continue

        board[move] = current

        if check_winner(current):
            print_board()
            print(f"Player {current} wins!")
            return

        current = 'O' if current == 'X' else 'X'

    print_board()
    print("It's a draw!")

play_game()