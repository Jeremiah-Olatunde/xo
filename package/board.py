class Board():

	def __init__(self, start = None, rowNo = 3, colNo = 3):

		self.rowNo = rowNo
		self.colNo = colNo

		self.board = self.buildBoard(rowNo, colNo) if not start else start
		self.clone = self.buildBoard(rowNo, colNo)

		print(self)

	def place(self, player, pos):

		xCoor, yCoor = self.coorConv(pos)
		
		self.board[xCoor][yCoor] = player
		
	def buildBoard(self, rows, cols):

		# UGLY CODE ALERT, I'M LAZY AT THE MOMENT
		board = [ [ x+y for y in range(1, cols+1)  ] for x in range(0, cols*(rows-1) + 1, cols) ]

		return board

	def coorConv(self, coor):

		for xItr, row in enumerate(self.clone):

			for yItr, data in enumerate(row):

				if data == coor:

					return [xItr, yItr]

	def __str__(self):

		rtnStr = '-'*40 + '\n'

		rowDiv = '\t' + '~~~~'*self.colNo + '~'

		for row in self.board:

			rowStr = '|'

			for col in row:

				rowStr += f' {col} |'

			rowStr = f'{rowDiv}\n\t{rowStr}\n'
			rtnStr += rowStr		

		return rtnStr + rowDiv + '\n'

