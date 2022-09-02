import os
import pygame

from src.settings import physics as p

class Player(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)

		self.game = game

		# surface initialization
		texture_name = "temp_player_placeholder"
		texture_path = os.path.join("assets", texture_name + ".png")
		self.image = pygame.image.load(texture_path).convert_alpha()
		self.rect = self.image.get_rect()

		# movement attributes
		self.velocity = pygame.math.Vector2(0, 0)
		self.position = pygame.math.Vector2(0, 0)
		self.direction = pygame.math.Vector2(0, 0)

		self.rect.x, self.rect.y = self.position

	def get_key_input(self):
		keys = pygame.key.get_pressed()
		return keys

	def handle_movement(self):
		keys = self.get_key_input()

		# sets the direction the player is trying to move the character
		if keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		cur_vel = self.velocity.x

		# either accelerates or decelerates the character depending on the direction
		if abs(self.direction.x) == 1: # if there is a direction
			calc_new_vel_x = cur_vel + (p.ACCELERATION.x  * self.direction.x)
			# ^ calculated new velocity
			new_x_vel = p.MAX_VEL.x * self.direction.x if abs(calc_new_vel_x) > p.MAX_VEL.x else calc_new_vel_x
			# ^ ensures new velocity doesn't exceed max velocity
			self.velocity.x = new_x_vel
		elif self.direction.x == 0 and self.velocity.x: # still moving, not touching the keys
			cur_direction = cur_vel / abs(cur_vel)
			print(cur_direction)
			calc_new_abs_vel_x = abs(cur_vel) - p.INERTIA.x
			new_x_vel = 0 if calc_new_abs_vel_x < 0 else calc_new_abs_vel_x * cur_direction
			self.velocity.x = new_x_vel

		self.position += self.velocity
		self.rect.x, self.rect.y = self.position

	def draw(self):
		self.game.WIN.blit(self.image, self.rect)

	def update(self):
		self.handle_movement()

		self.draw()

	
	# def define_movement_physics(self):
	# 	# Using a ratio unit ensures that the movement is equivalent across
	# 	# different sized windows
	# 	self.ratio_unit = ratio_unit = self.game.WIN.get_size()[0] / 1000

	# def handle_key_input(self, key_input):
	# 	keys = key_input
		
	# 	if keys[pygame.K_d]:
	# 		if self.h_vel <= self.MAX_H_VEL:
	# 			self.h_vel += self.H_ACC
	# 	elif keys[pygame.K_a]:
	# 		if self.h_vel >= (self.MAX_H_VEL * -1):
	# 			self.h_vel -= self.H_ACC
	# 	elif h_vel != 0:
	# 		direction = -1 if self.h_vel > 0 else 1
	# 		amount = self.H_INERTIA if (abs(self.h_vel) - self.H_INERTIA) > 0 else abs(self.h_vel)
	# 		self.h_vel += amount * direction

	# def handle_physics(self):
		
	# 	self.rect.x += self.h_vel

	# 	self.rect.y += 

	# def handle_collision(self):
