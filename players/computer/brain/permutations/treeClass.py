from .nodeClass import Node

class Tree():

	def __init__(self, movesArr):

		self.movesArr = movesArr
		self.root = None
		self.Node = Node

		self.buildTree()

	def buildTree(self):

		self.root = self.Node(0)

		def recurse(node, array, depth, string):

			for itr, x in enumerate(array):

				newString = string + str(x)

				node.child = (createdNode := self.Node(itr, x, node))

				copyArr = array[:]

				ommited = copyArr.pop(itr)

				recurse(createdNode, copyArr, depth + 1, newString)

		recurse(self.root, self.movesArr[:], 0, '')

	def __len__(self):

		return len(self.wordArr)