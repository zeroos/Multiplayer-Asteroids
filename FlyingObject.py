import pygame 

from Settings import Settings

class FlyingObject(pygame.sprite.Sprite):
        """basic class for all flying objects"""
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.move = [0,0]
                self.pos = [0,0] #position in floats [rect stores it in ints]
        def update(self):
                """flying around with constant speed and scrolling through borders"""
                self.pos[0] += self.move[0]
                self.pos[1] += self.move[1]
                if self.rect.bottom < 0:
                        self.rect.top = Settings.map_size[1]
                        self.pos[0], self.pos[1] = self.rect.center
                elif self.rect.top > Settings.map_size[1]:
                        self.rect.bottom = 0
                        self.pos[0], self.pos[1] = self.rect.center
                if self.rect.right < 0:
                        self.rect.left = Settings.map_size[0]
                        self.pos[0], self.pos[1] = self.rect.center
                elif self.rect.left > Settings.map_size[0]:
                        self.rect.right = 0
                        self.pos[0], self.pos[1] = self.rect.center

                self.rect.center = self.pos[0], self.pos[1]

