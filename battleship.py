import random


#ship classes
class Ship:
	ship_available = True

	def __init__(self, length, number):
		self.length = length
		self.number = number
		


	def rotate(self, horizontal, vertical):
		self.horizontal = horizontal
		self.vertical = vertical


class Carrier(Ship):
	def __init__(self, length, number):
		self.length = 5
		self.number = 1
		self.numer -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Battleship(Ship):
	def __init__(self, length, number):
		self.length = 4
		self.number = 1
		self.numer -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Cruiser(Ship):
	def __init__(self, length, number):
		self.length = 3
		self.number = 1
		self.numer -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Destroyer(Ship):
	def __init__(self, length, number):
		self.length = 2
		self.number = 2
		self.numer -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Submarine(Ship):
	def __init__(self, length, number):
		self.length = 1
		self.number = 2
		self.numer -= 1 
		if self.number < 1:
			Ship.ship_available = False

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



