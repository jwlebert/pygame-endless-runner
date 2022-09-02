import pygame
import sys

from src.settings import settings
from src.Player import Player
from src.mapping.Map import Map

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)

class Game:
	"""Represents the game."""
	def __init__(self):
		"""Initalizes the game."""

		# FPS Timer
		self.timer = pygame.time.Clock()
		self.FPS = settings.FPS

		# Screen initialization
		s_x = settings.SCREEN_WIDTH
		screen_size = settings.SCREEN_DIMENSIONS
		self.WIN = pygame.display.set_mode(screen_size)
		game_title = settings.TITLE
		pygame.display.set_caption(game_title)

		# Side scrolling initialization
		self.scroll_speed = (s_x * settings.SCROLL_FACTOR) / self.FPS
		self.x_scroll = 0

		# Map handler initialization
		self.map = Map(self)

		# Player initialization
		self.player = Player(self)

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
		self.player.update()

		pygame.display.update()

	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()