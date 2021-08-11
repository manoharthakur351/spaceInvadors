import pygame


class Player ():
	speed = 5
	bullets = []
	def __init__ (self, img, game, size = (110,110)):
		self.size = size
		self.img = pygame.image.load(img)
		self.img = pygame.transform.scale(self.img,self.size)
		self.game = game
		self.pos = [self.game.display_size[0]//2-(self.size[0]//2), self.game.display_size[1]]
		
	def move (self, dirn):
		if dirn == "left" and self.pos[0] <= self.game.display_size[0]  :
			self.pos[0] += self.speed
		if dirn == "right" and self.pos[0] >= 0  :
			self.pos[0] -= self.speed
		
	def set_bullet (self, bullet):
		self.bullet = bullet
		self.bullets.append(self.bullet)

	def fire (self):

		
		if self.bullet.has_spawned == False:
			self.bullet.spawn(self.pos[0], self.pos[1])
			
		self.bullet.visible()
		
		self.bullet.move()
		
		if self.bullet.pos[1] <= 0:
			self.bullet.pos[1] =self.game.display_size[1]-self.size[1]
			self.bullet.pos[0] = self.pos[0]
			self.bullet.spawn(self.pos[0], self.pos[1])
		
	def visible (self):
		""" function to display player on screen. """
		self.game.display.blit(self.img, self.pos)


