import pygame

# GAME ENVIRONMENT
class GameEnvironment ():
	is_on = False
	screen = None
	win_len_x = None
	win_len_y = None
	logo = None
	desc = None
	
	def __init__(self, win_len_x, win_len_y, colour = (0, 0, 0)):
		self.screen = pygame.display.set_mode((win_len_x,win_len_y))
		self.is_on = True
		return

