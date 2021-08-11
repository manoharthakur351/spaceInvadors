import pygame


class Bullet ():
	img = None
	height = 10
	width = 10
	speed = 30
	pos_x = None
	pos_y = None
	def __init__(self,img = None, speed = None, pos = None, size = None):
		self.width = size[0]
		self.height = size[1]
		self.speed = speed
		self.img = pygame.image.load(img)
		self.img = pygame.transform.scale(self.img,size)
		pass

	def move (self):
		self.pos_y -= self.speed
		