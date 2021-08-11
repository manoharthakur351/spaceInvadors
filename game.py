import pygame




class Environment ():
	game_count = 0
	def __init__ (self):
		self.display_size=(970, 1300)
		self.display = pygame.display.set_mode((self.display_size))
		self.is_on = True
		self.player_pos = []
	
	def count (self):
		self.game_count += 1
		return self.game_count
		
		
