import time

class Game():

	def __init__(self, Board, Player, AI, start = None):

		self.board = Board(start)
		self.player1 = AI(1, 'x', 'o')
		self.player2 = Player(2, 'o', 'x') 
		self.currentPlayer = self.player1
		self.playedMoves = []
		
		self.playGame()

	def playGame(self):
		
		move = self.currentPlayer.move(self.playedMoves, self.board)
		self.playedMoves.append(move)

		print(self.board)

		if self.checkWinner():
			
			print(f'Player {self.currentPlayer} WINS!!!')
			exit()

		self.switchPlayer()

		print(self.currentPlayer)

		if len(self.playedMoves) == 9: print(f'TIE!!!')
		else : self.playGame()

	def switchPlayer(self):

		if self.currentPlayer == self.player1: self.currentPlayer = self.player2

		else: self.currentPlayer = self.player1

	def checkWinner(self):

		def check(arr): 

			if arr[0] == arr[1] == arr[2]: return True
			else: return False

		for itr, row in enumerate(self.board.board):

			if check(row) == True: return True

		for i in range(3):

			col = [row[i] for row in self.board.board]

			if check(col) == True: return True

		diagonalI = [self.board.board[x][x] for x in range(3)]
		diagonalII = [self.board.board[x][2-x] for x in range(3)]

		if check(diagonalI) == True: return True
		if check(diagonalII) == True: return True

		return False

