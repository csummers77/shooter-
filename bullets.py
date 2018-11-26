import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
	def __init__(self,screen,the_player,direction):
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,0,5,20)
		self.color = (0,0,0)
		self.rect.centerx = the_player.x
		self.rect.top = the_player.y
		self.speed = 15
		self.direction = direction
		self.x = self.rect.x
		self.y = self.rect.y

	def update(self):
		if self.direction == 1: 
			self.y -= self.speed 
			self.rect.y = self.y 
		elif self.direction == 2: 
			self.x += self.speed 
			self.rect.x = self.x 
		elif self.direction == 3: 
			self.y += self.speed 
			self.rect.y = self.y 
		else: 
			self.x -= self.speed 
			self.rect.x = self.x 


	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect) 