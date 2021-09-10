import random


#ship classes
class Ship:
	ship_count = 0
	ship_available = True

	def __init__(self, length, number):
		self.length = length
		self.number = number
		self.ship_count -= 1
		if self.ship_count < 1:
			ship_available = False


	def rotate(self, horizontal, vertical):
		self.horizontal = horizontal
		self.vertical = vertical


class Carrier(Ship):
	def __init__(self, length, number):
		self.length = 5
		self.number = 1
		super().ship_count

class Battleship(Ship):
	def __init__(self, length, number):
		self.length = 4
		self.number = 1

class Cruiser(Ship):
	def __init__(self, length, number):
		self.length = 3
		self.number = 1

class Destroyer(Ship):
	def __init__(self, length, number):
		self.length = 2
		self.number = 2

class Submarine(Ship):
	def __init__(self, length, number):
		self.length = 1
		self.number = 2

#battlfield 0 = empty 1 is ship

battlefieldA = 	[0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,]

battlefieldB = 	[0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,]



#ship placement



