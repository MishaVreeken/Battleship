import random


#ship classes
class Ship:
	ship_available = True
	ship_quantity = [1, 1, 1, 2, 2]

	def __init__(self, ship_name, length):
		self.name = ship_name
		self.length = length

#battlfield 0 = empty. 1 = ship, 2 = hit, -1 = miss  met een while loop kan itereren

battlefieldPlayer = 	{"A1":0,"A2":0,"A3":0,"A4":0,"A5":0,"A6":0,"A7":0,"A8":0,"A9":0,"A10":0,
				"B1":0,"B2":0,"B3":0,"B4":0,"B5":0,"B6":0,"B7":0,"B8":0,"B9":0,"B10":0,
				"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0,"C10":0,
				"D1":0,"D2":0,"D3":0,"D4":0,"D5":0,"D6":0,"D7":0,"D8":0,"D9":0,"D10":0,
				"E1":0,"E2":0,"E3":0,"E4":0,"E5":0,"E6":0,"E7":0,"E8":0,"E9":0,"E10":0,
				"F1":0,"F2":0,"F3":0,"F4":0,"F5":0,"F6":0,"F7":0,"F8":0,"F9":0,"F10":0,
				"G1":0,"G2":0,"G3":0,"G4":0,"G5":0,"G6":0,"G7":0,"G8":0,"G9":0,"G10":0,
				"H1":0,"H2":0,"H3":0,"H4":0,"H5":0,"H6":0,"H7":0,"H8":0,"H9":0,"H10":0,
				"I1":0,"I2":0,"I3":0,"I4":0,"I5":0,"I6":0,"I7":0,"I8":0,"I9":0,"I10":0,
				"J1":0,"J2":0,"J3":0,"J4":0,"J5":0,"J6":0,"J7":0,"J8":0,"J9":0,"J10":0}

battlefieldComp = 	{"A1":0,"A2":0,"A3":0,"A4":0,"A5":0,"A6":0,"A7":0,"A8":0,"A9":0,"A10":0,
				"B1":0,"B2":0,"B3":0,"B4":0,"B5":0,"B6":0,"B7":0,"B8":0,"B9":0,"B10":0,
				"C1":0,"C2":0,"C3":0,"C4":0,"C5":0,"C6":0,"C7":0,"C8":0,"C9":0,"C10":0,
				"D1":0,"D2":0,"D3":0,"D4":0,"D5":0,"D6":0,"D7":0,"D8":0,"D9":0,"D10":0,
				"E1":0,"E2":0,"E3":0,"E4":0,"E5":0,"E6":0,"E7":0,"E8":0,"E9":0,"E10":0,
				"F1":0,"F2":0,"F3":0,"F4":0,"F5":0,"F6":0,"F7":0,"F8":0,"F9":0,"F10":0,
				"G1":0,"G2":0,"G3":0,"G4":0,"G5":0,"G6":0,"G7":0,"G8":0,"G9":0,"G10":0,
				"H1":0,"H2":0,"H3":0,"H4":0,"H5":0,"H6":0,"H7":0,"H8":0,"H9":0,"H10":0,
				"I1":0,"I2":0,"I3":0,"I4":0,"I5":0,"I6":0,"I7":0,"I8":0,"I9":0,"I10":0,
				"J1":0,"J2":0,"J3":0,"J4":0,"J5":0,"J6":0,"J7":0,"J8":0,"J9":0,"J10":0}


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


print(battlefieldPlayer) # print niet mooie
place = input("Where do you want to place {} (starting position)".format(Ship.name) )   # moet in de vorige loop verwerkt worden denk met classes voor de simpelheid.
verhor = input("And do you want to place it (H)orizontal or (V)ertical?")
while Ship.length >= 0:
	for keys, values in battlefieldPlayer.items():
		if keys == place:
			values == 1
	Ship.length -= 1


##### code for positioning ######
# verhor = input("Do you want to place it (H)orizontal or (V)ertical? ")  
# if verhor == "V" or "v":   #altering the choice doenst work yet
# 	verhor == "Vertical"
# if verhor == "H" or "h":
# 	verhor == "Horizontal"	
# print("Ok lets place it {}".format(verhor))

# place = input("where do you want to place the {}? ".format())


####start game here####
