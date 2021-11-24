import pygame as pg
import constants as cst

pg.init()

vec = pg.math.Vector2 

class Platform(pg.sprite.Sprite):
    def __init__(self, x,y,w,h, duckable=True, friction=-0.15):
        super().__init__()

        self.surf = pg.Surface((w, h))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (x, -y+cst.HEIGHT-h/2))
        self.duckable = duckable
        
        self.friction = friction
        self.being_ducked = False
        self.duck_duration = 500
        self.duck_start = 0

        self.needs_field = False
        self.field = None
        self._layer = 1

    def update(self, player):

        if self in player.platform_collisions:
            if player.ducking and not self.being_ducked:
                self.duck_start = pg.time.get_ticks()
                self.being_ducked = True

            if player.growing and self.field is None:
                self.needs_field = True


        if pg.time.get_ticks() - self.duck_start > self.duck_duration:
            self.being_ducked = False
            self.duck_start = 0
