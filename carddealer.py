import random

pile = []

def carddealer(numplayers):
	deck = deck()
	players = []
	for i in range(numplayers):
		players.append(humanplayer(i))
	while i < 52:
		for z in range(numplayers):
			players[z].deal(deck[i])
			i += 1


#makes the deck
def deck():
	deck = []
	for i in range(1, 53):
		deck.append(i)
	random.shuffle(deck)
	return deck

def play():
	pile.append()

