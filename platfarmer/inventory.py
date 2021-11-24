import pygame as pg
import constants as cst

class InventoryDisplay(pg.sprite.Sprite):

    def __init__(self, x=10,y=10,w=300,h=100, duckable=True, friction=-0.15):
        super().__init__()
        # self.window = pg.display.set_mode((w,h))
        # self.surf = pg.Surface((w, h)).convert()
        # self.surf.fill((0,0,0,0))
        # self.rect = self.surf.get_rect(center = (x, -y+cst.HEIGHT-h/2))
        # pg.draw.rect(self.surf, (255,0,0, 255), self.rect, width=1)

# class Inventory(pg.sprite.Sprite):

#     def __init__(self):


#         self.can = Can(10,10,64, 64)