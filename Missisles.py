import pygame
import math

import Utils
from  FlyingObject import FlyingObject
from Settings import *

class Missisle(FlyingObject):
	"""basic missisle"""
	#ideas:
	#accelerating missisles
	def __init__(self, pos, direction, speed, lifespan, init_move=[0,0]):
		FlyingObject.__init__(self)
		self.image, self.rect = Utils.loadImage("missisle_basic.png")

		self.move = [math.sin(math.radians(-direction))*speed, -math.cos(math.radians(direction))*speed]
		self.move[0] += init_move[0]
		self.move[1] += init_move[1]
		self.pos = pos#position of the center of the missisle, in floats [rect keeps it in ints]
		#rotate image
		self.image = pygame.transform.rotozoom(self.image, direction, 1)
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.lifespan = lifespan
		snd = Utils.loadSound("missisle_basic.ogg")
		vol_r = pos[0]/Settings.screen_size[0]
		vol_l = 1-vol_r
		try:
			snd.play().set_volume(vol_l,vol_r)
		except AttributeError:
			pass #not enaught channels
	def update(self):
		FlyingObject.update(self)
		self.lifespan -= 1
		if self.lifespan <= 0:
			self.kill()
	def collision(self, obj):
		pass

