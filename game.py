import pygame
import math



class Environment ():
	game_count = 0
	display_size=(970, 1300)
	enemy_spawn_area_x = [0, display_size[0]]
	enemy_spawn_area_y = [50,400]
	
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
	
	def set_weapon (self, weapon):
		self.weapon = weapon
		
