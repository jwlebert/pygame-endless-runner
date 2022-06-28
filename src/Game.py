import pygame
from src.Block import Block

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)

class Game:
	"""Represents the game."""
	def __init__(self, settings):
		"""Initalizes the game."""
		self.settings = settings

		# FPS Timer
		self.timer = pygame.time.Clock()
		self.FPS = self.settings["FPS"]

		# Screen initialization
		screen_size = self.settings["screen_size"]
		self.WIN = pygame.display.set_mode(screen_size)
		game_title = self.settings["game_title"]
		pygame.display.set_caption(game_title)

		# Side scrolling initialization
		self.x_scroll = 0

		self.blocks = [
			Block(self, {
				"dimensions": (100, 100),
				"color": BLACK,
				"init_pos": (500, 350)
			}),
			Block(self, {
				"dimensions": (200, 100),
				"color": BLACK,
				"init_pos": (600, 500)
			}),
			Block(self, {
				"dimensions": (50, 50),
				"color": BLACK,
				"init_pos": (800, 200)
			}),
		]

	def start(self):
		"""Starts the game."""
		self.active = True

		while self.active:
			self.loop()

	def loop(self):
		"""Executes the core gameplay loop. Should be run every tick."""
		self.handle_events()

		self.draw()

		self.x_scroll += self.settings["scroll_speed"]

		self.timer.tick(self.FPS)

	def draw(self):
		"""Draws everything to the screen."""
		self.WIN.fill(WHITE)

		for block in self.blocks:
			block.draw()

		pygame.display.update()

	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
