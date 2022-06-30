import pygame

class Block(pygame.sprite.Sprite):
	def __init__(self, game, data):
		pygame.sprite.Sprite.__init__(self)

		self.game = game
		self.data = data
		# DATA
		# "dimensions": (num, num),
		# "color": RGB, OR "texture": "<img>"
		# "init_pos": (num, num)

		if "color" in self.data:
			self.image = pygame.Surface(self.data["dimensions"])
			self.image.fill(self.data["color"])
		elif "texture" in self.data:
			path_to_img = f"assets/{self.data['texture']}.png"
			self.image = pygame.transform.scale(
				pygame.image.load(path_to_img), self.data["dimensions"]
			)

		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.data["init_pos"]

	def draw(self, origin):
		x_scroll = self.game.x_scroll
		init_pos = self.data["init_pos"]
		pos = (init_pos[0] + origin) - x_scroll, init_pos[1]

		self.rect.x, self.rect.y = pos

		if "color" in self.data:
			pygame.draw.rect(self.game.WIN, self.data["color"], self.rect)
		elif "texture" in self.data:
			self.game.WIN.blit(self.image, self.rect)

	# TODO : def tile() ; tile an image over a surface instead of
	# scaling it; scaling doesn't really work for patterned textures.