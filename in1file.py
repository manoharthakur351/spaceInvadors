import pygame
import random

pygame.init()

# display
screen = pygame.display.set_mode((970,1300))
screen_width = screen.get_size()[0]-200


# objects in the game
player_img = pygame.image.load("player.png")
bullet_img = pygame.image.load("bullet.png")
enemy_img = pygame.image.load("enemy.png")
player_img = pygame.transform.scale(player_img,(100,100))
bullet_img = pygame.transform.scale(bullet_img,(40,40))
enemy_img = pygame.transform.scale(enemy_img,(200,200))

# position of objects in the game
player_pos = [1070//2,1300]
bullet_pos = [1070//2, player_pos[1]]
enemy_pos = [1070//2,130]

#temp
x = 1
y = 1


# speeds
player_speed = 10
bullet_speed = 50
enemy_speed =  10


bullet_has_spawned = False

def show_score ():
	score_txt = font.render("score : "+str(score), True, (2,255,2))
	screen.blit(score_txt,(10,10))
# score
score = 0
font = pygame.font.Font("freesansbold.ttf",40)

while True:
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_4:
				player_speed = -10
			if event.key == pygame.K_6:
				player_speed = 10
			if event.key == pygame.K_0:
				player_speed  +=10
			if event.key == pygame.K_5:
				if not bullet_has_spawned:
					bullet_has_spawned = True
				else:
					bullet_has_spawned = False
				
	
	screen.fill((0,0,0))
	
	# enemy movements
	enemy_pos[0]+= enemy_speed
	if enemy_pos[0] <= 60 or enemy_pos[0] >= 810:
		enemy_speed = - enemy_speed
		enemy_pos[1] += 40
	if enemy_pos[1] >= 1300:
		enemy_pos[1] = 40
	

	# bullet movements
	
	
	#get_x_bullet = bullet_pos[0] 
	if bullet_has_spawned:
		if bullet_pos[1] <= 0:
			bullet_pos[1] =  player_pos[1]
			bullet_pos[0] =  player_pos[0]+30
			bullet_has_spawned == False
		else:
			bullet_pos[1]-= bullet_speed
	else:
		bullet_pos[0] = player_pos[0]+50-20

	# player movements
	player_pos[0]+= player_speed
	if player_pos[0] <= 0 or player_pos[0] >= 975:
		player_speed = 0
	



	# finish enemy
	if bullet_pos[0]+20 in range(enemy_pos[0],enemy_pos[0]+200):
		if abs(enemy_pos[y] - bullet_pos[y]) <= 200:
			enemy_pos = [1070//2,130]
			score+=1
	
	screen.blit(bullet_img,bullet_pos)
	screen.blit(enemy_img, enemy_pos )
	screen.blit(player_img,player_pos)
	show_score()
	pygame.display.flip() #update()
	pass

