class Player(object):
	def __init__(self):
		self.species = "human"

	def startGame(self):
		pass

	def move(self, board):
		x = int(input("x: "))
		y = int(input("y: "))
		return [x, y]

	def reward(self, value, board):
		pass

	def available_moves(self, board):
		moves = []
		for y in range(len(board)):
			for x in range(len(board[y])):
				if not board[y][x]:
					moves.append([x, y])
		return moves
