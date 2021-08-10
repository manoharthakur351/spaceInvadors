import pygame
import random

# initialising pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((900,600))

# pygame display and icon
pygame.display.set_caption("space")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# space
spaceImg = pygame.image.load('space_2.png')
spaceImg = pygame.transform.scale(spaceImg, (970+100,1400)) 

# player
playerImg = pygame.image.load('space-ship.png')
player_x = 400
player_y = 1300
playerImg = pygame.transform.scale(playerImg, (110,100)) 
player_x_change = 0

# enemy
enemyImg = pygame.image.load('enemy.png')
enemy_x = random.randint(0,970)
enemy_y = random.randint(100,300)
enemyImg = pygame.transform.scale(enemyImg, (150,130)) 
enemy_x_change = random.choice([1,-1])*4
enemy_y_change = 40

def player (x, y):
	"""blit-->drow"""
	screen.blit(playerImg,(x, y))

def enemy (x, y):
	"""blit-->drow"""
	screen.blit(enemyImg,(x, y))

def space (x, y):
	"""blit-->drow"""
	screen.blit(spaceImg,(x, y))


# game loop
running = True
while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		# check whether a key stroke pressed or not
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_4:
				player_x_change = -4
			if event.key == pygame.K_6:
				player_x_change = +4
		
	
	
	screen.fill((0,0,0))
	space (0, 0)
	#------------------
	
	player_x += player_x_change
	enemy_x += enemy_x_change
	
	# check that player do not go outside the main window
	if player_x <= 0:
		player_x_change = 0
	elif player_x >= 970:
		player_x_change = 970
	
	# enemy movement
	if enemy_x <= -50:
		enemy_x_change = 4
		enemy_y += enemy_y_change
	elif enemy_x >= 970:
		enemy_x_change = -4
		enemy_y += enemy_y_change
	
	
	
	player(player_x,player_y)
	enemy(enemy_x, enemy_y)
	
	pygame.display.update()

"""
screen_x should be 970
screen_y should be 1300
"""
