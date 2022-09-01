import os
import pygame

from src.Game import Game

class Block(pygame.sprite.Sprite):
	"""An informal interface for different types of blocks."""
	def __init__(self, game: Game):
		"""Initialize the sprite."""
		pygame.sprite.Sprite.__init__(self)

		self.game = game
	
	def draw(self, origin):
		"""Draws the sprite to the screen."""
		pass

class Coloured_Block(Block):
	"""A block which is textured with a colour."""
	def __init__(self, game: Game, data):
		"""Initializes the sprite."""
		Block.__init__(self, game)

		# Storing the data as class variables
		self.color = data["color"]
		self.dimensions = data["dimensions"]
		self.init_pos = data["init_pos"]

		self.image = pygame.Surface(self.dimensions)
		self.image.fill(self.color)

		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.init_pos

	def draw(self, origin):
		"""Draws the block to the screen."""
		x_scroll = self.game.x_scroll
		init_pos = self.init_pos
		pos = (init_pos[0] + origin) - x_scroll, init_pos[1]
		# ^ enables side scrolling

		self.rect.x, self.rect.y = pos

		pygame.draw.rect(self.game.WIN, self.color, self.rect)

class Textured_Block(Block):
	"""A block which is textured using a texture image."""
	def __init__(self, game: Game, data):
		"""Initializes the block."""
		Block.__init__(self, game)

		# Storing the data as class variables
		self.dimensions = data["dimensions"]
		self.tiling = data.get("tile?", False)
		self.init_pos = data["init_pos"]
		self.texture_file_name = data["texture"] + ".png"

		self.img_path = os.path.join('assets', self.texture_file_name)
		self.texture = pygame.image.load(self.img_path).convert()

		# either tiles or scales the selected texture
		if self.tiling:
			self.tile()
		else:
			self.image = pygame.transform.scale(
				pygame.image.load(self.img_path), self.dimensions
			)
		
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.init_pos

	def draw(self, origin):
		"""Draws the sprite to the screen."""
		x_scroll = self.game.x_scroll
		init_pos = self.init_pos
		pos = (init_pos[0] + origin) - x_scroll, init_pos[1]

		self.rect.x, self.rect.y = pos

		self.game.WIN.blit(self.image, self.rect)
	
	def tile(self):
		"""
		Tiles the sprite so that it doesn't appear distorted even on
		blocks bigger than the sprite itself.
		"""
		self.image = pygame.Surface(self.dimensions)

		width, height = self.dimensions
		t_width, t_height = self.texture.get_size()

		columns = int((width // t_width) + 1)
		rows = int((height // t_height) + 1)

		for row in range(0, rows):
			for col in range(0, columns):
				self.image.blit(
					pygame.image.load(self.img_path).convert(), 
					(col * t_width, row * t_height))