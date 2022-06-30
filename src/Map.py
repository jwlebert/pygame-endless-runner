import random
import copy

from src.Block import Block

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Room:
	def __init__(self, width, tiles):
		self.width = width
		self.tiles = tiles

		self.origin = 0
	
	def load(self):
		return self

	def set_origin(self, origin):
		self.origin = origin
	
	def draw(self):
		for tile in self.tiles:
			tile.draw(self.origin)

class Map:
	def __init__(self, game):
		self.game = game
		
		self.loaded_rooms = []

		self.next_spawn_point = 0

		s_x, s_y = self.game.WIN.get_size()

		beginning_room = Room(s_x, [
			Block(self.game, { 
				"dimensions": (s_x, s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			})])

		beginning_room.set_origin(self.next_spawn_point)
		
		self.next_spawn_point += beginning_room.width

		self.loaded_rooms.append(beginning_room)

	def draw(self):
		for i, room in enumerate(self.loaded_rooms):
			print(i, room.tiles[0].rect.x)
			room.draw()

	def load_rooms(self):
		self.clear_rooms()
		self.populate_rooms()		

	def clear_rooms(self):
		living_rooms = list(filter(
			lambda r: ((r.origin + r.width) - self.game.x_scroll) > 0,
			self.loaded_rooms
			))

		self.loaded_rooms = living_rooms

	def populate_rooms(self):
		print(len(self.loaded_rooms))
		if len(self.loaded_rooms) < 6:
			rooms = self.loaded_rooms

			spawn_point = self.next_spawn_point

			templates = self.generate_rooms()

			new_room = copy.copy(random.choice(templates))
			new_room.set_origin(spawn_point)
			rooms.append(new_room)
			spawn_point += new_room.width

			spacer = self.generate_spacer()
			spacer.set_origin(spawn_point)
			rooms.append(spacer.load())
			spawn_point += spacer.width

			self.next_spawn_point = spawn_point

			self.loaded_rooms = rooms
	
	def generate_spacer(self):
		s_x, s_y = self.game.WIN.get_size()
		return Room(s_x * (3/12), [
			Block(self.game, {
				"dimensions": (s_x * (3/12), s_y * (1/12)),
				"texture": "hazard_thick",
				"init_pos": (0, s_y * (11/12)),
			})
		])

	def generate_rooms(self):
		rooms = []

		s_x, s_y = self.game.WIN.get_size()
		# 12 x 12 grid 

		rooms.append(Room(s_x, [ # simple 1 platform
			Block(self.game, { # floor
				"dimensions": (s_x, s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			}),
			Block(self.game, { # platform
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (4/12), s_y * (7/12)),
			}) # TODO : add prize here
		]))

		rooms.append(Room(s_x, [
			Block(self.game, { # floor left
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			}),
			Block(self.game, { # floor right
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (8/12), s_y * (11/12)),
			}),
			Block(self.game, { # platform
				"dimensions": (s_x * (5/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (7/24), s_y * (6/12)),
			})
		]))

		rooms.append(Room(s_x, [
			Block(self.game, { # floor ; enemy
				"dimensions": (s_x, s_y * (1/12)),
				"color": BLACK,
				"init_pos": (0, s_y * (11/12)),
			}),
			Block(self.game, { # platform 1 (lowest) ; small reward
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (2/12), s_y * (8/12)),
			}),
			Block(self.game, { # platform 2 ; enemy
				"dimensions": (s_x * (4/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (5/12), s_y * (5/12)),
			}),
			Block(self.game, { # platform 3 (highest) ; big reward
				"dimensions": (s_x * (3/12), s_y * (1/12)),
				"color": BLACK,
				"init_pos": (s_x * (8/12), s_y * (2/12)),
			}),
		]))

		return rooms