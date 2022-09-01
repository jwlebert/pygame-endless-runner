import random

from src.mapping.Block import Block
from src.mapping.Room import *

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Map:
	"""Represents the map that the plater traverses."""
	def __init__(self, game):
		"""Initializes the map."""
		self.game = game

		self.load_blueprints()

		self.next_x_spawn = 0

		starter_room = self.starter_room_blueprint.build(self.next_x_spawn)
		
		self.next_x_spawn += starter_room.width

		self.loaded_rooms = []
		self.max_loaded_rooms = 6
		self.loaded_rooms.append(starter_room)
	
	def load_blueprints(self):
		"""Creates all blueprints for this map and stores them."""
		self.starter_room_blueprint = Starter_Room_Blueprint(self.game)
		self.spacer_blueprint = Spacer_Blueprint(self.game)
		self.blueprints = [
			Basic_Platform_Blueprint(self.game),
			Basic_Pit_Blueprint(self.game),
			Ascending_Platforms_Blueprint(self.game)
		]

	def load_rooms(self):
		"""Creates new rooms and removes old rooms, as needed."""
		self.clear_rooms()
		self.populate_rooms()		

	def clear_rooms(self):
		"""Clears rooms after the screen scrolls past them."""
		living_rooms = list(filter(
			lambda r: ((r.x_origin + r.width) - self.game.x_scroll) > 0,
			self.loaded_rooms
			))

		self.loaded_rooms = living_rooms

	def populate_rooms(self):
		"""
		Ensures there is always a certain number of rooms by creating new
		ones after old ones are removed.
		"""
		if len(self.loaded_rooms) < self.max_loaded_rooms:
			rooms = self.loaded_rooms

			spawn_point = self.next_x_spawn

			blueprints = self.blueprints

			random_blueprint = random.choice(blueprints)
			new_room = random_blueprint.build(spawn_point)
			rooms.append(new_room)
			spawn_point += new_room.width

			spacer = self.spacer_blueprint.build(spawn_point)
			rooms.append(spacer)
			spawn_point += spacer.width

			self.next_x_spawn = spawn_point

			self.loaded_rooms = rooms

	def draw(self):
		"""Draws all entities in the currently loaded rooms."""
		for room in self.loaded_rooms:
			room.draw()