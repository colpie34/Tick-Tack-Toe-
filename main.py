def tic_tac_toe():
    """A two-player console Tic Tac Toe game using a magic square for win detection."""

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    magic_square = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    def print_board():
        print()
        print(f" {board[0]} | {board[1]} | {board[2]}")
        print("---|---|---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---|---|---")
        print(f" {board[6]} | {board[7]} | {board[8]}")
        print()

    def get_number():
        while True:
            try:
                number = int(input("Enter a position (1-9): "))
                if 1 <= number <= 9:
                    return number
                print("Number must be between 1 and 9.")
            except ValueError:
                print("Please enter a valid number.")

    def turn(player):
        while True:
            position = get_number() - 1

            if board[position] in ["X", "O"]:
                print("That position is already occupied.")
            else:
                board[position] = player
                break

    def check_win(player):
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if (
                            board[x] == player
                            and board[y] == player
                            and board[z] == player
                            and magic_square[x]
                            + magic_square[y]
                            + magic_square[z]
                            == 15
                        ):
                            print_board()
                            print(f"Player {player} wins!")
                            return True

        if all(space in ["X", "O"] for space in board):
            print_board()
            print("The game ends in a tie!")
            return True

        return False

    while True:
        print_board()
        print("Player X's turn")
        turn("X")

        if check_win("X"):
            break

        print_board()
        print("Player O's turn")
        turn("O")

        if check_win("O"):
            break


if __name__ == "__main__":
    tic_tac_toe()
