import pygame
import random
from player import Player
from game import GameEnvironment
# INITIALISING PYGAME
pygame.init()




# __Main__
# game specific variables
window_size = [970, 1300]
game = GameEnvironment(*window_size)
player = Player("space-ship.png",20, game)
player.setBullet('space_1.png')

# player specific variables
player_dirn= ""

# game loop 
while game.is_on:
	game.screen.fill((2,4,44))
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_6:
				player_dirn = "right"
			if event.key == pygame.K_4:
				player_dirn ="left"
			if event.key == pygame.K_4:
				
				player.fire()
			
	player.spawn()
	player.move(12,player_dirn)
	
	pygame.display.update()