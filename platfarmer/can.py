import pygame as pg
import constants as cst


class Can(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):

        super().__init__()
        self.surf = pg.image.load('./resources/can.png').convert_alpha()
        self.surf = pg.transform.scale(self.surf, (w, h))
        self.rect = self.surf.get_rect(center = (x, -y+cst.HEIGHT-h/2))
        self._layer = 0