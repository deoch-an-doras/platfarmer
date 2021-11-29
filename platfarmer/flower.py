import pygame as pg
import constants as cst


class Flower(pg.sprite.Sprite):

    def __init__(self, x, y, size=None, volume=5000):

        super().__init__()
        self.surf = pg.image.load('./resources/flower.png').convert_alpha()
        if size is None:
            self.w, self.h = self.size = self.surf.get_size() 
        else:
            self.w, self.h = self.size = size
        self.surf = pg.transform.scale(self.surf, self.size)
        self.rect = self.surf.get_rect(center = (x, cst.HEIGHT-self.h/2-y))
        self.volume = volume
        self._layer = 0
    
    def update(self, player):
        pass
