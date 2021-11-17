import pygame as pg
vec = pg.math.Vector2  # 2 for two dimensional


class Camera():

    def __init__(self, size):
        #
        self.W, self.H = self.size = size
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 


    def update(self, pos):
        self.pos.y = pos.y-self.H/2
        if self.pos.y > 0:
            self.pos.y = 0
        # self.pos.y= 0
        print(self.pos.y, pos.y)