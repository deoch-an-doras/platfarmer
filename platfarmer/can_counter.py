import pygame as pg
import constants as cst

from can import Can

class CanCounter(pg.sprite.Sprite):

    def __init__(self):
        self.can = Can(10,10,64, 64)