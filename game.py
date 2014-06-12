import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5


#### Put class definitions here ####

class Rock(GameElement):
	IMAGE = "Rock" # This is a class attribute, called "IMAGE."
	SOLID = True

class Character(GameElement):
	IMAGE = "Girl" # making a class attribute IMAGE, containing a value of "Girl"

	def next_pos(self, direction):
		if direction == "up":
			return (self.x, self.y-1)
		elif direction == "down":
			return (self.x, self.y+1)
		elif direction == "left":
			return (self.x-1, self.y)
		elif direction == "right":
			return (self.x+1, self.y)
		return None  

	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))


class Gem(GameElement):
	IMAGE = "BlueGem"
	SOLID = False

####   End class definitions    ####

def initialize():
	"""game initialization code here"""
	global PLAYER
	PLAYER = Character()
	GAME_BOARD.register(PLAYER)
	GAME_BOARD.set_el(2, 2, PLAYER)
	print PLAYER

	GAME_BOARD.draw_msg("This game is wicked awesome.")

	#list of rock position
	rock_positions = [
			(2, 1),
			(1, 2),
			(3, 2),
			(2, 3),
		]

	rocks = []

	for pos in rock_positions:
		rock = Rock()
		GAME_BOARD.register(rock)
		GAME_BOARD.set_el(pos[0],pos[1], rock)
		rocks.append(rock)

	rocks[-1].SOLID = False # making the bottom-most rock as intangible

	# # Initialize and register rock 1
	# rock1 = Rock() # This creates an instance, rock1, of a class, Rock().
	# GAME_BOARD.register(rock1)
	# GAME_BOARD.set_el(2, 1, rock1)

	# # Initialize and register rock 2
	# rock2 = Rock()
	# GAME_BOARD.register(rock2)
	# GAME_BOARD.set_el(1, 2, rock2)

	# # Initialize and register rock 3
	# rock3 = Rock()
	# GAME_BOARD.register(rock3)
	# GAME_BOARD.set_el(3, 2, rock3)

	# # Initialize and register rock 4
	# rock4 = Rock()
	# GAME_BOARD.register(rock4)
	# GAME_BOARD.set_el(2, 3, rock4)

	# # print where the rocks are
	# print "The first rock is at", (rock1.x, rock1.y)
	# print "The second rock is at", (rock2.x, rock2.y)

	for rock in rocks:
		print rock

	# add gem instance
	gem = Gem()
	GAME_BOARD.register(gem)
	GAME_BOARD.set_el(3, 1, gem)


def keyboard_handler():
	"""This sets the motion for the character object."""
	direction = None 

	if KEYBOARD[key.UP]:
		direction = "up"
		GAME_BOARD.draw_msg("You pressed up.")

		# next_y = PLAYER.y - 1
		# GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
		# GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
	if KEYBOARD[key.DOWN]:
		direction = "down"
		GAME_BOARD.draw_msg("You pressed down.")

		# next_y = PLAYER.y + 1
		# GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
		# GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
	if KEYBOARD[key.LEFT]:
		direction = "left"
		GAME_BOARD.draw_msg("You pressed left.")

		# next_x = PLAYER.x - 1
		# GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
		# GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
	if KEYBOARD[key.RIGHT]:
		direction = "right"
		GAME_BOARD.draw_msg("You pressed right.")
		# next_x = PLAYER.x + 1
		# GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
		# GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
	if KEYBOARD[key.SPACE]:
		GAME_BOARD.erase_msg()

	if direction:
		next_location = PLAYER.next_pos(direction)
		next_x = next_location[0]
		next_y = next_location[1]

		existing_el = GAME_BOARD.get_el(next_x, next_y)

		if existing_el:
			existing_el.interact(PLAYER)

		if existing_el is None or not existing_el.SOLID:
			# if none or not SOLID, walk through
			GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
			GAME_BOARD.set_el(next_x, next_y, PLAYER)

def __init__(self):
	GameElement.__init__(self)
	self.inventory = []





