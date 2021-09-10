import random


#ship classes
class Ship:
	ship_available = True
	ship_names ["Carrier", ]

	def __init__(self, ship_name, length, number):
		self.name = ship_name
		self.length = length
		self.number = number
	
	def rotate(self, horizontal, vertical):
		self.horizontal = horizontal
		self.vertical = vertical


class Carrier(Ship):
	def __init__(self, ship_name, length, number):
		super().__init__(self, ship_name = "Carrier", length = 5, number = 1) 
		self.number -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Battleship(Ship):
	def __init__(self, length, number):
		super().__init__(self, ship_name = "Battleship", length = 4, number = 1) 
		self.number -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Cruiser(Ship):
	def __init__(self, length, number):
		super().__init__(self, ship_name = "Cruiser", length = 3, number = 1)
		self.number -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Destroyer(Ship):
	def __init__(self, length, number):
		super().__init__(self, ship_name = "Destroyer", length = 2, number = 2)
		self.number -= 1 
		if self.number < 1:
			Ship.ship_available = False

class Submarine(Ship):
	def __init__(self, length, number):
		super().__init__(self, ship_name = "Submarine", length = 1, number = 2)
		self.number -= 1 
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



#ship placement by players

while ship_available = True:
	shipChoice = input("What ship do you want to place?")
	for ship in Ship.ship_names:
		if shipChoice == ship_names(ship):
			print("You have chosen to place {}".format(ship_names(ship))
			verthor = input("Do you want to place it Horizontal or Vertical?")
			if verthor != "Vertical" or "Horizontal":
				print("THAT IS NOT AN OPTION")

		else:
			print("Your chosesn ship: {} is not an option".fomrmat(shipChoice))
			break





