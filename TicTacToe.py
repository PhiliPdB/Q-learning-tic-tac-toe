class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.player1, self.player2 = player1, player2
        self.turn = 1
        self.score = {'Player1wins': 0, 'Player2wins': 0, 'Ties': 0}

    def play_game(self):
        # Let this function handle the gameplay
        # Initialize players
        self.player1.startGame()
        self.player2.startGame()
        while True:
            if self.turn is 1:
                player, other_player = self.player1, self.player2
            else:
                player, other_player = self.player2, self.player1

            if player.species is "human":
                self.print_board()

            # Ask for players move
            move = player.move(self.board)
            if self.board[move[1]][move[0]]:
                # Can't place move
                break
            # Place move
            self.board[move[1]][move[0]] = self.turn

            # See if the game has ended
            if self.player_wins(self.turn):
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                if self.turn is 1:
                    self.score['Player1wins'] += 1
                else:
                    self.score['Player2wins'] += 1
                break
            if self.board_full(): # Tie
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                self.score['Ties'] += 1
                break
            other_player.reward(0, self.board)
            self.turn *= -1

    def player_wins(self, turn):
        # print('check win for turn %d' % turn)
        for x in self.board:
            if sum(x) is 3 * turn:
                # print('win for player %d' % turn)
                return True

        scored1 = scored2 = 0
        for x in range(3):
            scored1 += self.board[x][x]
            scored2 += list(reversed(self.board[x]))[x]
            score = 0
            for y in range(3):
                score += self.board[y][x]
            if score is 3 * turn:
                # print('win for player %d' % turn)
                return True

        if scored1 is 3 * turn or scored2 is 3 * turn:
            # print('win for player %d' % turn)
            return True

        return False

    def board_full(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True

    def print_board(self):
        printed_board = []

        for row in self.board:
            printed_row = []
            for entry in row:
                if entry == 0:
                    printed_row.append('   ')
                elif entry == 1:
                    printed_row.append(' X ')
                elif entry == -1:
                    printed_row.append(' O ')
            printed_board.append(printed_row)

        print(printed_board[0][0] + '|' + printed_board[0][1] + '|' + printed_board[0][2])
        print("-----------")
        print(printed_board[1][0] + '|' + printed_board[1][1] + '|' + printed_board[1][2])
        print("-----------")
        print(printed_board[2][0] + '|' + printed_board[2][1] + '|' + printed_board[2][2])
