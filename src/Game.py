import pygame

# from src.Block import Block
from src.mapping.Map import Map

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
		screen_size = s_x, s_y = self.settings["screen_size"]
		self.WIN = pygame.display.set_mode(screen_size)
		game_title = self.settings["game_title"]
		pygame.display.set_caption(game_title)

		# Side scrolling initialization
		self.scroll_speed = (s_x * self.settings["scroll_factor"]) / self.FPS
		self.x_scroll = 0

		# Map handler initialization
		self.map = Map(self)

	def start(self):
		"""Starts the game."""
		self.active = True

		while self.active:
			self.loop()

	def loop(self):
		"""Executes the core gameplay loop. Should be run every tick."""
		self.handle_events()

		self.map.load_rooms()

		self.draw()

		self.x_scroll += self.scroll_speed

		self.timer.tick(self.FPS)

	def draw(self):
		"""Draws everything to the screen."""
		self.WIN.fill(WHITE)

		self.map.draw()

		pygame.display.update()

	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()