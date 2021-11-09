import pygame as pg
import constants as cst

pg.init()

vec = pg.math.Vector2  # 2 for two dimensional

class Platform(pg.sprite.Sprite):
    def __init__(self, x,y,w,h):
        super().__init__()
        self.surf = pg.Surface((w, h))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (x, y))