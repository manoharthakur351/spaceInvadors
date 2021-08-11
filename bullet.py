import pygame


class Bullet ():
	
	def __init__ (self, img, game, player = None, speed = 60, size = (40,40)):
		self.img = pygame.image.load(img)
		self.img = pygame.transform.scale(self.img, size)
		self.player = player
		self.pos = [self.player.pos[0],self.player.pos[1]]
		self.game = game
		self.speed = speed
		self.has_spawned = False
		self.size = size
		
	def spawn (self,x ,y):
		self.game.display.blit(self.img,(x+37,y))
		self.pos_after_spawn = [x+37]
		self.has_spawned = True
		
		
	def move (self):
		"""function to move the bullet in upward direction"""
		self.pos[1] -= self.speed
	
	def visible (self):
		""" function to display player on screen. """
		#self.pos = [self.player.pos[0],self.player.pos[1]]
		self.game.display.blit(self.img, [self.pos_after_spawn[0],self.pos[1]+100])
		
	

		
	