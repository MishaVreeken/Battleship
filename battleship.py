import random


#ship classes
class Ship:
	ship_available = True
	ship_quantity = [1, 1, 1, 2, 2]

	def __init__(self, ship_name, length, number):
		self.name = ship_name
		self.length = length
		self.number = number
	
	def rotate(self, horizontal, vertical):
		self.horizontal = horizontal
		self.vertical = vertical


# class Carrier(Ship):
# 	def __init__(self, ship_name, length, number):
# 		super().__init__(self, ship_name = "Carrier", length = 5, number = 1) 
# 		self.number -= 1 
# 		if self.number < 1:
# 			Ship.ship_available = False

# class Battleship(Ship):
# 	def __init__(self, length, number):
# 		super().__init__(self, ship_name = "Battleship", length = 4, number = 1) 
# 		self.number -= 1 
# 		if self.number < 1:
# 			Ship.ship_available = False

# class Cruiser(Ship):
# 	def __init__(self, length, number):
# 		super().__init__(self, ship_name = "Cruiser", length = 3, number = 1)
# 		self.number -= 1 
# 		if self.number < 1:
# 			Ship.ship_available = False

# class Destroyer(Ship):
# 	def __init__(self, length, number):
# 		super().__init__(self, ship_name = "Destroyer", length = 2, number = 2)
# 		self.number -= 1 
# 		if self.number < 1:
# 			Ship.ship_available = False

# class Submarine(Ship):
# 	def __init__(self, length, number):
# 		super().__init__(self, ship_name = "Submarine", length = 1, number = 2)
# 		self.number -= 1 
# 		if self.number < 1:
# 			Ship.ship_available = False

#battlfield 0 = empty 1 is ship

battlefieldPlayer = 	[0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,]

battlefieldBot = 	[0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,
				0,0,0,0,0,0,0,0,0,0,]



#ship placement by players give list of ships with quantity and substract it from the pool after placement

while Ship.ship_available == True:
	x = input("Pick a ship to place: \n"
		"1 Carrier (Quantity: {Carrier})\n"
		"2 Battleship (Quantity: {Battleship})\n"
		"3 Cruiser (Quantity: {Cruiser})\n"
		"4 Destroyer (Quantity: {Destroyer})\n"
		"5 Submarine (Quantity: {Submarine})\n".format(Carrier = Ship.ship_quantity[0], Battleship = Ship.ship_quantity[1], Cruiser = Ship.ship_quantity[2], Destroyer = Ship.ship_quantity[3], Submarine = Ship.ship_quantity[4]))

	if x == "1":
		if Ship.ship_quantity[0] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[0] -= 1
			verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")  
			if verhor == "V" or "v":   #altering the choice doenst work yet
				verhor == "Vertical"
			if verhor == "H" or "h":
				verhor == "Horizontal"	
			print("Ok lets place it {}".format(verhor))

	if x == "2":
		if Ship.ship_quantity[1] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[1] -= 1
			verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")
			print("Ok lets place it {}".format(verhor))

	if x == "3":
		if Ship.ship_quantity[2] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[2] -= 1
			verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")
			print("Ok lets place it {}".format(verhor))

	if x == "4":
		if Ship.ship_quantity[3] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[3] -= 1
			verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")
			print("Ok lets place it {}".format(verhor))

	if x == "5":
		if Ship.ship_quantity[4] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[4] -= 1
			verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")
			print("Ok lets place it {}".format(verhor))

	else:
		print("That wasn't an option")  #this line shouldnt be printed after a choice is made need to fix



