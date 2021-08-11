# ENEMY CLASS
class Enemy (Player):
	speed = 10
	img = None
	
	def __init__ (self, img, speed):
		self.speed = speed
		img = pygame.image.load(img)

	def spawn (self):
		self.pos_x = random.randint(0, 1070)
		self.pos_y = random.randint(0, 1070)
	
	def move (self):
		self.pos_x += self.speed
		if self.pos_x >= 970 or self.pos_y <= 0:
			self.speed = -self.speed
			self.pos_y += 40