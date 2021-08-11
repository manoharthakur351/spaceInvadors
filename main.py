import pygame
import game
from player import Player
from bullet import Bullet

pygame.init()

# game specific variables
game = game.Environment()


# player specific variables
player = Player("player.png", game)
player_movement_dirn = ""
player_is_firing = False

# bullet specific variables
bullet = Bullet("bullet.png", game = game, player = player)
player.set_bullet(bullet)


# GAME LOOP
while game.is_on :
	game.count()
	
	# CONTROLS
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_6:
				player_movement_dirn = "left"
			if event.key == pygame.K_4:
				player_movement_dirn = "right"
			if event.key == pygame.K_5:
				player_is_firing = True			
	
	game.display.fill((0, 28, 28))
	# THINGS BECOME VISIBLE FROM HERE
	
	# handling the player
	player.move(player_movement_dirn)
	player.visible()
	
	# handling the bullet
	if player_is_firing:
		if player.bullet.has_spawned == False:
			player.bullet.spawn()
		player.bullet.visible()
		player.bullet.move()
		
	
	pygame.display.update()
	pass # GAME LOOP END



