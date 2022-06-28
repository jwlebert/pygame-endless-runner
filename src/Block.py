import pygame

class Block(pygame.sprite.Sprite):
	def __init__(self, game, data):
		pygame.sprite.Sprite.__init__(self)

		self.game = game
		self.data = data

		self.image = pygame.Surface(self.data["dimensions"])
		self.image.fill(self.data["color"])

		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.data["init_pos"]

	def draw(self):
		x_scroll = self.game.x_scroll
		init_pos = self.data["init_pos"]
		pos = init_pos[0] - x_scroll, init_pos[1]

		self.rect.x, self.rect.y = pos

		pygame.draw.rect(self.game.WIN, self.data["color"], self.rect)