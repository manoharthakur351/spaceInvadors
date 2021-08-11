import pygame
import bullet


class Player ():
	game = None
	speed = 20
	pos_x = 970//2
	pos_y = 1300
	img = None
	bullet = None
	height = 100
	width = 100
	bullet = None
	bullets = []
	def __init__ (self, img, speed, game):
		self.speed = speed
		self.img = pygame.image.load(img)
		self.img = pygame.transform.scale(self.img,(self.height,self.width))
		self.game = game

	def setBullet (self, mybullet):
		self.bullet = mybullet
		
	def spawn (self):
		self.game.screen.blit(self.img,(self.pos_x, self.pos_y))
	
	def move (self, speed, dir):
		
		if dir == "left":
			self.pos_x -= self.speed
		if dir == "right":
			self.pos_x += self.speed
		
		if self.pos_x <= 0 :
			self.pos_x = 0
		if self.pos_x >= 970:
			self.pos_x = 970
	
	def fire (self):
		if self.bullet == None:
			print('bullet not set')
			return
		else :
			self.bullets.append(self.bullet)
			for abullet in self.bullets:
				pass
			
		
	
	
