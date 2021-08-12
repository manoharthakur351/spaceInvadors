import pygame
import random

class Enemy ():
	
	def __init__ (self, img, opponent= None, game = None):
		self.speed = 10
		self.pos = [0,0]
		self.opponent = opponent
		self.size_ = random.randint(100,200)
		self.size = (self.size_ ,self.size_ )
		self.img = pygame.image.load(img)
		self.img = pygame.transform.scale(self.img, self.size)
		self.has_spawned = True
		self.game = game

	def spawn (self):
		self.has_spawned = True
		self.pos[0] = random.randint(*self.game.enemy_spawn_area_x)
		self.pos[1] = random.randint(*self.game.enemy_spawn_area_y)
		self.size_ = random.randint(100,200)
		self.size = (self.size_ ,self.size_ )
	def move(self):
		self.pos[0] += self.speed
		
		if self.pos[0] >= self.game.display_size[0] or self.pos[0] <= 0:
			self.speed = -self.speed
			self.pos[1] += 40
			
	def visible (self):
		""" function to display player on screen. """
		#self.pos = [self.player.pos[0],self.player.pos[1]]
		self.game.display.blit(self.img, [self.pos[0],self.pos[1]])
	


