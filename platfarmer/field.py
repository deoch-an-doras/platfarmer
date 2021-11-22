import pygame as pg
from matplotlib.colors import ListedColormap
import numpy as np

def make_cmap(col1, col2, N):
    vals = np.ones((N, 4))
    for idx, (c1, c2) in enumerate(zip(col1, col2)):
        vals[:, idx] = np.linspace(c1/256, c2/256, N)
    newcmp = ListedColormap(vals)
    return newcmp

class Field(pg.sprite.Sprite):

    def __init__(self, platform):
        super().__init__()

        self.platform = platform
        self.w, self.x, self.y = platform.rect.width, platform.rect.centerx, platform.rect.top
        self.h = 10
        self.surf = pg.Surface((self.w, self.h))

        self.green  = (4, 188, 43)
        self.brown = (101, 57, 33)
        self.age_levels = 4

        self.cmap = make_cmap(self.green, self.brown, self.age_levels)

        self.birth_time = pg.time.get_ticks()
        self.death_time = self.birth_time + 5000
        self.age_ticks = 0
        self.age_level = 0
        self.age_fraction = 0
        self.color=self.green
        self.surf.fill(self.color)
        self.growing=False

        self.rect = self.surf.get_rect(center = (self.x, self.y))

    def update_color(self):
        self.color = tuple([int(i*255) for i in self.cmap(self.age_level)])
        self.surf.fill(self.color) 

    def update_age(self):
        self.age_ticks = min(self.death_time, max(0, pg.time.get_ticks() - self.birth_time))
        self.age_fraction = self.age_ticks/self.death_time
        self.age_level = int(self.age_fraction*self.age_levels)

        
    def update(self):
        if self.growing:
            self.birth_time += 200
            self.birth_time = min(self.birth_time, pg.time.get_ticks())
        
        self.update_age()
        self.update_color()