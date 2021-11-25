import pygame as pg
import constants as cst


class Can(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, volume=5000):

        super().__init__()
        self.surf = pg.image.load('./resources/can.png').convert_alpha()
        self.surf = pg.transform.scale(self.surf, (w, h))
        self.rect = self.surf.get_rect(center = (x, cst.HEIGHT-h/2-y))
        self.volume = volume
        self._layer = 0
    
    def update(self, player):
        if self in player.collisions:
            player.water += self.volume
            self.kill()
