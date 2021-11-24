import pygame as pg

vec = pg.math.Vector2

class Camera():

    def __init__(self, size):
        self.W, self.H = self.size = size
        self.pos = vec(0,0)

    def update(self, pos):
        self.pos.y = min(0, pos.y-self.H/2)

    def translate(self, sprite):
        return (sprite.rect.x, sprite.rect.y-self.pos.y)
                        