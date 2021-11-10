import pygame as pg
import constants as cst

pg.init()

vec = pg.math.Vector2 

class Platform(pg.sprite.Sprite):
    def __init__(self, x,y,w,h, duckable=True, friction=-0.15):
        super().__init__()
        
        self.surf = pg.Surface((w, h))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (x, y))
        self.duckable = duckable
        self.friction = friction
        self.being_ducked = False
        self.duck_duration = 500
        self.duck_start = 0


    def update(self):
        if pg.time.get_ticks() - self.duck_start > self.duck_duration:
            self.being_ducked = False
            self.duck_start = 0