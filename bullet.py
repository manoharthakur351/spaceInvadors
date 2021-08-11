import pygame


class Bullet ():
	
	def __init__ (self, img, game, player = None, speed = 1, size = (40,40)):
		self.img = pygame.image.load(img)
		self.img = pygame.transform.scale(self.img, size)
		self.player = player
		self.pos = [self.player.pos[0],self.player.pos[1]]
		self.game = game
		self.speed = speed
		self.has_spawned = False
		self.size = size
		
	def spawn (self):
		self.desired_spawn = [self.player.pos[0]+(self.player.size[0]//2)-self.size[0]//2 ]
		self.game.display.blit(self.img, [self.desired_spawn[0] ,self.player.pos[1]])
		self.has_spawned = True
		self.pos_after_spawn = [None,None]
		self.pos_after_spawn[0] = self.desired_spawn[0]

	def move (self):
		"""function to move the bullet in upward direction"""
		#self.pos = [self.player.pos[0],self.player.pos[1]]
		print(self.pos[1],end = " ")
		self.pos[1] -= self.speed
		print(self.pos[1])
		
		
	
	def visible (self):
		""" function to display player on screen. """
		#self.pos = [self.player.pos[0],self.player.pos[1]]
		self.game.display.blit(self.img, [self.pos_after_spawn[0],self.pos[1]])
		
	

		
	