import pygame
from pygame.locals import *
import math
import cmath
import random

import Utils
from  FlyingObject import FlyingObject
from Settings import *

class Asteroid(FlyingObject):
	"""asteroid"""
	#ideas:
	#accelerating missisles
	def __init__(self, size=200, pos=None, direction=None, speed=None):
		FlyingObject.__init__(self)
		self.size = size
                self.image = pygame.Surface((size, size))
		self.image.fill(Color(255,0,255))
                self.image.set_colorkey(Color(255,0,255))
		pointlist = []
		for i in range(random.randint(7,12)):#how much verticles
			x = random.randint(0,size//2)
			y1 = (size//2)**2 - x**2
			y1 = int(math.sqrt(y1))

			y2 = (size//4)**2 - x**2
			try:
				y2 = int(math.sqrt(y2))
			except ValueError:
				y2 = 0
			
				

			y = random.randint(y2, y1)

			y = random.choice([-1,1])*y
			x = random.choice([-1,1])*x

			y+=size//2
			x+=size//2

			pointlist += [(x,y)]
		s=size//2
		def cmp(a,b):
			if a==b: return 0
			if a[1] >= s and b[1] >= s:
				if a[0] > b[0]: return 1
				else: return -1
			if a[1] < s and b[1] < s:
				if a[0] > b[0]: return -1
				else: return 1
			if a[1] < s and b[1] >= s:
				return 1
			else:
				return -1

			
		pointlist.sort(cmp)
		#print pointlist
		self.rect = pygame.draw.polygon(self.image, Color(40,40,40), pointlist)
		self.rect = pygame.draw.polygon(self.image, Color(200,200,200), pointlist,3)
		#self.image, self.rect = Utils.loadImage("spaceship.png")
	
		if not pos:	
			#random position
			site = random.randint(0,1)
			br_pos = [0,0]
			br_pos[site] = 0
			br_pos[not site] = random.randint(0,Settings.map_size[not site])
			self.rect.bottomright = br_pos
			self.pos[0], self.pos[1] = self.rect.center#position of the center of the asteroid, in floats [rect keeps it in ints]
		else:
			self.pos = pos
			self.rect.center = pos
		
		if not direction:
			#random direction
			directions = range(360)
			del(directions[0])
			del(directions[90])
			del(directions[180])
			direction = random.choice(directions)

		if not speed:
			#random speed
			speed = random.randint(1,2)
		
		self.move = [math.sin(math.radians(-direction))*speed, -math.cos(math.radians(direction))*speed]
		self.mask = pygame.mask.from_surface(self.image)
	def collision(self, obj):
		pass
	def kill(self):
		if self.size > 30:
			pos1 = [] + self.pos
			pos2 = [] + self.pos
			Asteroid(self.size//2, pos1).add(self.groups())
			Asteroid(self.size//2, pos2).add(self.groups())
		FlyingObject.kill(self)
