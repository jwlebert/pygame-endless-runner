from src.mapping.Block import Coloured_Block, Textured_Block

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED =	(255, 0,   0)

class Room:
	"""A collection of blocks."""
	def __init__(self, width, x_origin, entities):
		"""Initializes the room."""
		self.width = width
		self.entities = entities
		self.x_origin = x_origin
	
	def draw(self):
		"""Draws all of the entities in the room."""
		for entity in self.entities:
			entity.draw(self.x_origin)

# TODO : Switch blueprints to a 24 grid instead of 12

# Blueprints are essentially presets of rooms. Each one represents a different
# room. To create a new room, make a new Blueprint subclass and add it to
# the list of blueprints in the map class.

class Blueprint:
	"""An informal interface for creating subclasses capable of generating preset rooms."""

	def __init__(self, game):
		"""Initializes the blueprint."""
		self.game = game

	def build(self, x_origin: int) -> Room:
		"""Creates and returns a room."""
		pass

class Starter_Room_Blueprint(Blueprint):
	"""
	An empty space where the player starts.
	"""
	def __init__(self, game):
		"""Initializes the blueprint."""
		Blueprint.__init__(self, game)
	
	def build(self, x_origin):
		"""Creates and returns the starter room."""
		s_x, s_y = self.game.WIN.get_size()
		return Room(s_x, x_origin, [
			Coloured_Block(self.game, { 
				"dimensions": (s_x, s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			})])

class Spacer_Blueprint(Blueprint):
	"""
	An empty space room which serves to seperate the rooms from each other.
	Every other room should be a spacer room.
	"""
	def __init__(self, game):
		"""Initializes the blueprint."""
		Blueprint.__init__(self, game)
	
	def build(self, x_origin):
		"""Creates and returns a spacer room."""
		s_x, s_y = self.game.WIN.get_size()
		return Room(s_x * (3/12), x_origin, [
			Coloured_Block(self.game, { # the floor
				"dimensions": (s_x * (3/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			})
		])

class Basic_Platform_Blueprint(Blueprint):
	"""
	A simple room that consists of a floor and a single platform in the middle.
	"""
	def __init__(self, game):
		"""Initializes the blueprint."""
		Blueprint.__init__(self, game)
	
	def build(self, x_origin):
		"""Creates and returns a basic platform room."""
		s_x, s_y = self.game.WIN.get_size()
		return Room(s_x, x_origin, [
			Coloured_Block(self.game, { # floor
				"dimensions": (s_x, s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			}),
			Coloured_Block(self.game, { # platform
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (4/12), s_y * (7/12)),
			}) # TODO : add prize here
		])

class Basic_Pit_Blueprint(Blueprint):
	"""
	A simple room that consists of a floor with a pit and a single platform
	above it.
	"""
	def __init__(self, game):
		"""Initializes the blueprint."""
		Blueprint.__init__(self, game)
	
	def build(self, x_origin):
		"""Creates and returns a basic pit room."""
		s_x, s_y = self.game.WIN.get_size()
		return Room(s_x, x_origin, [
			Coloured_Block(self.game, { # floor left
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			}),
			Coloured_Block(self.game, { # floor right
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (8/12), s_y * (11/12)),
			}),
			Coloured_Block(self.game, { # platform
				"dimensions": (s_x * (5/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (7/24), s_y * (6/12)),
			})
		])

class Ascending_Platforms_Blueprint(Blueprint):
	"""
	A room with multiple ascending platforms.
	"""
	def __init__(self, game):
		"""Initializes the blueprint."""
		Blueprint.__init__(self, game)
	
	def build(self, x_origin):
		"""Creates and returns a basic pit room."""
		s_x, s_y = self.game.WIN.get_size()
		return Room(s_x, x_origin, [
			Coloured_Block(self.game, { # floor ; enemy
				"dimensions": (s_x, s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			}),
			Coloured_Block(self.game, { # platform 1 (lowest) ; small reward
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (2/12), s_y * (8/12)),
			}),
			Coloured_Block(self.game, { # platform 2 ; enemy
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (5/12), s_y * (5/12)),
			}),
			Coloured_Block(self.game, { # platform 3 (highest) ; big reward
				"dimensions": (s_x * (3/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (8/12), s_y * (2/12)),
			}),
		])