#!/usr/bin/env python2

import os, pygame, random
from pygame.locals import *

from Settings import *
from Spaceship import *
from Asteroids import *
import Utils



class FpsMeter():
	def __init__(self):
		self.font = pygame.font.Font(None, 20)
	def update(self):
		self.fps = self.font.render(str(int(clock.get_fps()))+"fps", 1, (70, 70, 70))
	def draw(self, surface, x=10, y=10):
		surface.blit(self.fps, (x,y))	
		return self.fps.get_rect().move((x,y))

class Background():
	def __init__(self):
		self.surface = pygame.Surface(Settings.map_size)
		self.surface.fill(Color(0,0,0))
		for i in range(0, random.randint(30,500)):
			c = random.randint(50, 245)
			rc = c+random.randint(-10, 10)
			gc = c+random.randint(-10, 10)
			bc = c+random.randint(-10, 10)
			pos = (random.randint(0, Settings.map_size[0]), random.randint(0, Settings.map_size[1]))
			pygame.draw.circle(self.surface, Color(rc, gc, bc), pos, 0)
	def update(self):
		pass
	def draw(self, surface):
		surface.blit(self.surface, (0,0))		
	


def main():
	"""main function"""
	if not pygame.font:
		print("Cannot initialize fonts.")
		return
	global clock
	clock = pygame.time.Clock()
	pygame.init()
	if Settings.fullscreen:
		screenFlags = pygame.FULLSCREEN
		#screen_size is the resolution of the screen
	else:
		screenFlags = pygame.RESIZABLE
	screen = pygame.display.set_mode(Settings.screen_size, screenFlags)
	pygame.display.set_caption('Multiplayer Asteroids')
	pygame.mouse.set_visible(0)

	
	background = Background()
	fpsMeter = FpsMeter()
	

	#set up sprites
	allsprites = pygame.sprite.RenderUpdates()
	spaceships = pygame.sprite.RenderUpdates()
	missisles = pygame.sprite.RenderUpdates()
	asteroids = pygame.sprite.RenderUpdates()

	spaceship = Spaceship([Settings.map_size[0]//3, Settings.map_size[1]//2])
	spaceship2 = Spaceship([(Settings.map_size[0]*2) //3, Settings.map_size[1]//2])
	asteroid = Asteroid()
	allsprites.add(spaceship, spaceship2,  asteroid)
	asteroids.add(asteroid)
	spaceships.add(spaceship, spaceship2)

	pygame.display.flip()
	while True:
		#main game loop
		clock.tick(50) #fps
		

		for event in pygame.event.get():

			if event.type == USEREVENT and event.code == 0: #someone fired a missisle
				event.missisle.add(allsprites, missisles)
			elif event.type == KEYDOWN:
				if event.key == 273:	#up
					spaceship.startAccel()
				elif event.key == 119: 	#w
					spaceship2.startAccel()
				elif event.key == 274:	#down
					pass
				elif event.key == 115:	#s
					pass
				elif event.key == 275:	#right
					spaceship.startTurnRight()
				elif event.key == 97:	#a
					spaceship2.startTurnRight()
				elif event.key == 276:	#left
					spaceship.startTurnLeft()
				elif event.key == 100:	#d
					spaceship2.startTurnLeft()
				elif event.key == 109:	#m
					spaceship.shoot()
				elif event.key == 114:	#r
					spaceship2.shoot()
				elif event.key == 27:	#esc
					return
			elif event.type == KEYUP:
				if event.key == 273:	#up
					spaceship.stopAccel()
				elif event.key == 119: 	#w
					spaceship2.stopAccel()
				elif event.key == 274:	#down
					pass	
				elif event.key == 115:	#s
					pass
				elif event.key == 275:	#right
					spaceship.stopTurning()
				elif event.key == 97:	#a
					spaceship2.stopTurning()
				elif event.key == 276:	#left
					spaceship.stopTurning()
				elif event.key == 100:	#d
					spaceship2.stopTurning()
	
			elif event.type == QUIT:
				return


		fpsMeter.update()
		allsprites.update()


		#pygame.sprite.spritecollide(spaceship, asteroids, True)
		pygame.sprite.groupcollide(asteroids, missisles, True, True)
		pygame.sprite.groupcollide(asteroids, spaceships, True, True)
		pygame.sprite.groupcollide(spaceships, missisles, True, True)

		if pygame.sprite.collide_rect(spaceship, spaceship2):
			spaceship.kill()
			spaceship2.kill()

		if not len(asteroids.sprites())>0:#no asteroids
			asteroid = Asteroid()
			asteroids.add(asteroid)
			allsprites.add(asteroid)


		pygame.display.update([background.draw(screen), fpsMeter.draw(screen)] + allsprites.draw(screen))
		#pygame.display.flip()

if __name__ == '__main__':
	main()
