import pygame

# Player movement values
MAX_VEL = pygame.math.Vector2(100, 0)
# The terminal velocity of the player.

ACCELERATION = pygame.math.Vector2(2, 12)
# The y acceleration will be high. Basically, when the player jumps,
# they will have the acceleration value added to their y velocity.
# Because it'll only be added once, we need a high y acceleration and a
# comparatively small y deceleration so that we can jump.

INERTIA = pygame.math.Vector2(2.0, 9.8)
# Don't know if inertia is the right word for this, but basically it's
# the deceleration rate (x) and the gravity (y)