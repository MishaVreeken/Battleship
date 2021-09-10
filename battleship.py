class Ship:
	def __init__(self, length, number):
		self.length = length
		self.number = number

class Carrier(Ship):
	def __init__(self, length, number):
		self.length = 5
		self.number = 1

class Battleship(Ship):
	def __init__(self, length, number):
		self.length = 4
		self.number = 2

class Destroyer(Ship):
	def __init__(self, length, number):
		self.length = 3
		self.number = 3

class Submarine(Ship):
	def __init__(self, length, number):
		self.length = 3
		self.number = 4

class PatrolBoat(Ship):
	def __init__(self, length, number):
		self.length = 2
		self.number = 5