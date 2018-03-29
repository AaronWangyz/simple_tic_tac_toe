import random


class Game:
    def __init__(self):
        self.board = [[], [], []]
        self.column = 0
        self.row = 0
        self.i = 0

    def start_of_game(self):
        self.board = [["#", "#", "#"],
                      ["#", "#", "#"],
                      ["#", "#", "#"]]

    def print_board(self):
        for item in self.board:
            print(*item)

    def take_input(self):
        self.column = int(input("Please indicate column (1-3): \n"))
        self.row = int(input("Please indicate row (1-3): \n"))

    def make_move(self, player):
        if self.board[self.row - 1][self.column - 1] == "#":
            self.board[self.row - 1][self.column - 1] = player
        else:
            print("Position took! Please re-enter! \n")
            self.take_input()
            self.make_move(player)

    def check_win(self, player):
        self.i = 0

        while self.i < 2:
            if self.board[self.i][0] == player \
                    and self.board[self.i][0] == self.board[self.i][1] \
                    and self.board[self.i][0] == self.board[self.i][2]:
                print("Player ", player, " Win!\n")
                return True

            if self.board[0][self.i] == player \
                    and self.board[0][self.i] == self.board[1][self.i] \
                    and self.board[0][self.i] == self.board[2][self.i]:
                print("Player ", player, " Win!\n")
                return True

            if self.board[0][0] == player \
                    and self.board[0][0] == self.board[1][1] \
                    and self.board[0][0] == self.board[2][2]:
                print("Player ", player, " Win!\n")
                return True

            if self.board[0][2] == player \
                    and self.board[0][2] == self.board[1][1] \
                    and self.board[0][2] == self.board[2][0]:
                print("Player ", player, " Win!\n")
                return True
            else:
                self.i += 1

        return False


if __name__ == "__main__":
    player1 = "x"
    player2 = "o"
    toggle = {player1: player2, player2: player1}
    player = player1

    if random.choice([True, False]):
        player = "x"
    else:
        player = "o"

    print("Player '", player, "' go first!\n")

    temp = Game()

    temp.start_of_game()
    temp.print_board()

    while not temp.check_win(player):
        temp.take_input()
        temp.make_move(player)
        temp.print_board()
        if temp.check_win(player):
            quit()
        player = toggle[player]
