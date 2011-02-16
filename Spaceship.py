import pygame
from pygame.locals import *
import math

import Utils
from FlyingObject import FlyingObject
from Settings import *
from Missisles import Missisle

class Spaceship(FlyingObject):
	def __init__(self, pos=None):
		FlyingObject.__init__(self)
		
		self.spaceship, self.rect = Utils.loadImage("spaceship.png")
		self.flame = [Utils.loadImage("flame_red_00.png")[0], Utils.loadImage("flame_red_01.png")[0], Utils.loadImage("flame_red_02.png")[0]]

		self.flameRect = self.flame[0].get_rect()
		self.rect.h += self.flameRect.h

		self.flameRect.bottom = self.rect.h-self.flameRect.h
		self.flameRect.left = 0
		self.image = pygame.Surface((self.rect.w, self.rect.h))
		self.image.fill(Color(255,0,255))
		self.image.blit(self.spaceship, (0,0))
		self.spaceship = self.image.copy()
		self.spaceship.set_colorkey(Color(255,0,255))

		self.accel = False
		self.flameCounter = 0
		self.direction = 0
		self.turning = 0
		if pos == None:
			self.pos = [Settings.map_size[0]//2, Settings.map_size[1]//2]
		else:
			self.pos = pos
		self.snd_engine = Utils.loadSound("engine.ogg")
		self.snd_engine_channel = None

#		self.mask =  pygame.mask.from_surface(self.image)
	def update(self):
		self.direction += self.turning*Settings.turning_speed

		self.image = self.spaceship.copy()
		if self.accel:
			self.move[0] += math.sin(math.radians(-self.direction))*Settings.spaceship_accel
			self.move[1] += -math.cos(math.radians(self.direction))*Settings.spaceship_accel
			#show flames
			self.image.blit(self.flame[self.flameCounter], self.flameRect)
			self.flameCounter = (self.flameCounter+1)%3
			vol_r = abs(self.pos[0]/Settings.screen_size[0])
			if vol_r > 1:
				vol_r = 1
			vol_l = 1-vol_r

			if self.snd_engine_channel:
				self.snd_engine_channel.set_volume(vol_l, vol_r)
		
		#rotate image
	
		self.image = pygame.transform.rotate(self.image, self.direction)
		#create new rect, which will center itself properly
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

		FlyingObject.update(self)
	def collision(self, obj):
		pass
	def startAccel(self):
		self.accel = True	
		self.snd_engine_channel = self.snd_engine.play(-1)
	def stopAccel(self):
		self.accel = False
		self.snd_engine.stop()
	def startTurnRight(self):
		self.turning = -1
	def startTurnLeft(self):
		self.turning = 1
	def stopTurning(self):	
		self.turning = 0
	def shoot(self):
		missisle_distance = 10 #distance from the ship to the missisle [prevents ship from destroying itself each time it shoots]
		pos = [self.rect.center[0], self.rect.center[1]]
		pos[0] += math.sin(math.radians(-self.direction))*(self.rect.w//2+missisle_distance)
		pos[1] += -math.cos(math.radians(self.direction))*(self.rect.h//2+missisle_distance)
		init_move = [self.move[0], self.move[1]]

		speed = 10				# SHOULD BE CHANGED
		lifespan = 50				#
		pygame.event.post(pygame.event.Event(USEREVENT, {"code": 0, "missisle": Missisle(pos, self.direction, speed, lifespan, init_move)}))


