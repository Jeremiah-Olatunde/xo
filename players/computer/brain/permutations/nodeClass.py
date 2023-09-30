
class Descriptor():
	
	def __set__(self, instance, value):

		instance.childCount += 1
		varName = 'child_' + str(value.idx)
		instance.__dict__[varName] = value

class Node():

	child = Descriptor()

	def __init__(self, idx, data = 'root', parent = None, turn = None):

		self.idx = idx
		self.data = data
		self.parent = parent
		self.childCount = 0
		self.eval = None
		self.turn = turn

	def __repr__(self):

		return f'[Node => {self.idx}, Data => {self.data}, Eval => {self.eval}]'

	def __str__(self):

		return str(self.data)