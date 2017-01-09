from copy import deepcopy
from random import random, choice
from Player import Player


class QLearningPlayer(Player):
	def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
		self.species = "computer"
		self.q = {} # (state, action) keys: Q values
		self.epsilon = epsilon # Chance of random exploration
		self.alpha = alpha # Learning rate
		self.gamma = gamma # Discount factor

	def startGame(self):
		self.last_board = [[0 for x in range(3)] for y in range(3)]
		self.last_move = None

	def getQ(self, state, action):
		# Do this so it can write to self.q
		state = ",".join(str(cell) for row in state for cell in row)
		action = ",".join(str(i) for i in action)
		# encourage exploration
		# 'Optimistic' 1.0 initial values
		if self.q.get((state, action)) is None:
			self.q[(state, action)] = 1.0
		return self.q.get((state, action))

	def move(self, board):
		self.last_board = deepcopy(board)
		actions = self.available_moves(board)

		if random() < self.epsilon:
			# Go on exploration
			self.last_move = choice(actions)
			return self.last_move

		# Get list with Q values
		q_list = [self.getQ(self.last_board, action) for action in actions]
		maxQ = max(q_list)

		if q_list.count(maxQ) > 1:
			# Choose a random best option
			best_options = [i for i in range(len(actions)) if q_list[i] is maxQ]
			i = choice(best_options)
		else:
			i = q_list.index(maxQ)

		self.last_move = actions[i]
		return actions[i]

	def reward(self, value, board):
		if self.last_move:
			self.learn(self.last_board, self.last_move, value, deepcopy(board))

	def learn(self, state, action, reward, result_state):
		previous = self.getQ(state, action)
		max_q_new = max([self.getQ(result_state, action) for action in self.available_moves(state)])
		# Q function
		state = ",".join(str(cell) for row in state for cell in row)
		action = ",".join(str(i) for i in action)
		self.q[(state, action)] = previous + self.alpha * ((reward + self.gamma  * max_q_new) - previous)

	# For saving and loading the q
	def saveQ(self, file_name="q"):
		with open(file_name + ".txt", "w") as file:
			file.write(repr(self.q))

	def loadQ(self, file_name="q"):
		with open(file_name + ".txt", "r") as file:
			file = file.read()
			try:
				self.q = eval(file)
			except ValueError:
				self.q = {}
