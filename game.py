import pygame
import math
pygame.font.init()


class Environment ():
	game_count = 0
	display_size=(970, 1300)
	enemy_spawn_area_x = [0, display_size[0]]
	enemy_spawn_area_y = [50,110]
	score = 0
	font = pygame.font.Font("freesansbold.ttf",40)
	def __init__ (self):
		self.display = pygame.display.set_mode((self.display_size))
		self.is_on = True
		self.player_pos = []
		
	
	def count (self):
		self.game_count += 1
		return self.game_count
	
	def set_players (self, player, enemy):
		self.player = player
		self.enemy = enemy
	
	def finish_enemy (self):
		self.players_x_gap = self.weapon.pos[0]- self.enemy.pos[0]
		self.players_y_gap = self.weapon.pos[1]- self.enemy.pos[1]
		self.net_gap = math.pow(self.players_x_gap,2)+math.pow(self.players_y_gap,2)
		self.net_gap_true = math.sqrt(self.net_gap)
		if self.net_gap_true <= 50:
			self.enemy.spawn()
			self.score += 1
	
	def set_weapon (self, weapon):
		self.weapon = weapon
	
	
	def show_text (self, text):
		text = self.font.render(text, True, (255, 255, 255))
		self.display.blit(text,(10,10))
	
	
	