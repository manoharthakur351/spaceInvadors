import pygame
import game
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()

# game specific variables
game = game.Environment()


# player specific variables
player = Player("player.png", game)
player_movement_dirn = ""
player.is_firing = False

# bullet specific variables
bullet = Bullet("bullet.png", game = game, player = player)
player.set_bullet(bullet)

# enemy
enemy = Enemy("enemy.png", opponent = player, game = game)

game.set_players(player, enemy)
game.set_weapon(bullet)
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
			if event.key == pygame.K_1:
				player.speed -= 5
			if event.key == pygame.K_3:
				player.speed += 5
			if player.speed <= 0:
				player.speed += 5
			if event.key == pygame.K_5:
				if player.is_firing == False:
					player.is_firing = True
				elif player.is_firing == True:
					player.is_firing = False		
	
	game.display.fill((0, 28, 28))
	# THINGS BECOME VISIBLE FROM HERE

	# handling the bullet
	if player.is_firing:
		player.fire()
		
	# handling enemy
	if not enemy.has_spawned:
		enemy.spawn()
	enemy.move()
	enemy.visible()
	
	# handling the player
	player.move(player_movement_dirn)
	player.visible()
	

	game.finish_enemy()
	
	pygame.display.update()
	pass # GAME LOOP END



