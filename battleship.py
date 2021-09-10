import random


#ship classes
class Ship:
	ship_available = True
	ship_quantity = [1, 1, 1, 2, 2]

	def __init__(self, ship_name, length):
		self.name = ship_name
		self.length = length

#battlfield 0 = empty. 1 = ship, X = hit, - = miss

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
ship = []
player = input("What is your name?: ")

print("OK! {} Lets start a game of Battleship".format(player))
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
			ship = Ship("Carrier", 5)
#			return ship 
	elif x == "2":
		if Ship.ship_quantity[1] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[1] -= 1
			ship = Ship("Battleship", 4)
#			return ship
	elif x == "3":
		if Ship.ship_quantity[2] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[2] -= 1
			ship = Ship("Cruiser", 3)
#			return ship
	elif x == "4":
		if Ship.ship_quantity[3] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[3] -= 1
			ship = Ship("Destroyer", 2)
#			return ship
	elif x == "5":
		if Ship.ship_quantity[4] <= 0:
			print("No more ships available")
		else:
			Ship.ship_quantity[4] -= 1
			ship = Ship("Submarine", 1)
	#		return ship
	else:
		print("That wasn't an option") 

	if sum(Ship.ship_quantity) == 0:
		Ship.ship_available = False

##### code for positioning ######
# verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")  
# if verhor == "V" or "v":   #altering the choice doenst work yet
# 	verhor == "Vertical"
# if verhor == "H" or "h":
# 	verhor == "Horizontal"	
# print("Ok lets place it {}".format(verhor))

# place = input("where do you want to place the {}? ".format())


####start game here####
