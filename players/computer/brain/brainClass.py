from .permutations.treeClass import Tree

class Brain():

	def __init__(self, symbol, opponentSymbol):

		self.Tree = Tree
		self.symbol = symbol
		self.opponentSymbol = opponentSymbol
		self.currentPlayer = self.symbol
		self.board = None

	def evaluate(self, moves, node):

		self.simulateGame(moves)
		state = self.evaluateState(self.board.board)

		if state == True : node.eval = 1
		elif state == False: node.eval = -1
		elif state == None: node.eval = 0

		self.resetBoard(moves)

		return node.eval
		
	def simulateGame(self, moves):

		moves = [int(x) for x in moves]

		for itr, x in enumerate(moves):

			self.board.place(self.currentPlayer, x)
			self.switchPlayer()

		self.currentPlayer = self.symbol

	def evaluateState(self, board):

		def check(arr): 

			if arr[0] == arr[1] == arr[2]: 

				return True if arr[0] == self.symbol else False

		for itr, row in enumerate(board):

			if check(row) is not None: return check(row)

		for i in range(3):

			col = [row[i] for row in board]

			if check(col) is not None: return check(col)

		diagonalI = [board[x][x] for x in range(3)]
		diagonalII = [board[x][2-x] for x in range(3)]

		if check(diagonalI) is not None: return check(diagonalI)
		if check(diagonalII) is not None: return check(diagonalII)

		return None

	def resetBoard(self, moves):

		for x in moves:

			self.board.place(int(x), int(x))

	def switchPlayer(self):

		if self.currentPlayer == self.symbol: self.currentPlayer = self.opponentSymbol
		else: self.currentPlayer = self.symbol
		