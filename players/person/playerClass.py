class Player():

	def __init__(self, iD, symbol, opponentSymbol):

		self.iD = iD
		self.symbol = symbol
		self.moves = []

	def move(self, moves, board):

		validMoves = [x for x in range(1,10) if x not in moves]
		chosenMove = self.getInput(validMoves)
		self.moves.append(chosenMove)
		board.place(self.symbol, chosenMove)
		
		return chosenMove

	def getInput(self, validMoves):

		chosenMove = input(f'Current Player ("{self}") => ')
		if chosenMove == 'exit': exit()

		try: 

			chosenMove = int(chosenMove)
			if chosenMove not in validMoves: raise TypeError
			else: return chosenMove

		except: 

			print(f'INVALID INPUT')
			chosenMove = self.getInput(validMoves)
			
		return chosenMove		

	def __str__(self):

		return self.symbol