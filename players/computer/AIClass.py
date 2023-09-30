from .brain.brainClass import Brain
import random

class AI():

	def __init__(self, iD, symbol, opponentSymbol):

		self.iD = iD

		self.symbol = symbol

		self.opponentSymbol = opponentSymbol

		self.brain = Brain(self.symbol, self.opponentSymbol)

		self.tree = None


	def move(self, playedMoves, board):

		self.brain.board = board

		possibleMoves = [x for x in range(1,10) if x not in playedMoves]

		if len(playedMoves) == 0: finalMove = 1 
		elif len(playedMoves) == 1: finalMove = 5
		else:

			self.tree = self.brain.Tree(possibleMoves)

			self.ponderMoves()

			self.minMax()

			finalMove = int(str(self.tree.root.eval))

		self.brain.board.place(self.symbol,finalMove)
		
		return finalMove

	def ponderMoves(self):

		def recurse(node, string = '', depth = 0):

			for x in range(node.childCount):

				childNode = node.__dict__['child_' + str(x)]
				childNode.turn = self.symbol if depth%2 == 0 else self.opponentSymbol

				movesString = string + str(childNode)

				finalEval = self.brain.evaluate(movesString, childNode)

				if finalEval != 0: continue

				recurse(childNode, movesString, depth + 1)

		recurse(self.tree.root)

	def minMax(self):

		def recurse(node, depth = 0):

			toSort = []

			for x in range(node.childCount):

				childNode = node.__dict__['child_' + str(x)]

				if childNode.childCount > 0: recurse(childNode, depth + 1)

				if childNode.eval == None: return None

				toSort.append(childNode)

			if depth%2 == 0: chosenNode = self.sort(toSort, 'max')
			else: chosenNode = self.sort(toSort, 'min')


			if node.data == 'root': node.eval = chosenNode
			else: node.eval = chosenNode.eval

		recurse(self.tree.root)

	@staticmethod
	def sort(array, sortType):
		print(array)
		base = array[0]

		if sortType == 'max':

			for x in array:

				if x.eval > base.eval: base = x

		if sortType == 'min':

			for x in array:

				if x.eval < base.eval: base = x
                                                                                                                                                                                                                                                                         
		eq = None

		for x in array:

			if x == base == 1 and eq != False: eq = True
			else: eq = False

		if eq == True: base.eval = sum(array)

		return base		

	def __str__(self):

		return self.symbol