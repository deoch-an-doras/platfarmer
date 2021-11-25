import pygame as pg
import constants as cst

class InventoryDisplay(pg.sprite.Sprite):

    def __init__(self, w=300, h=100):
        super().__init__()
        self.bboxsurf = pg.Surface((w, h)).convert_alpha()
        self.bboxsurf.fill((0,0,0,0))
        self.bboxrect = self.bboxsurf.get_rect(topleft = (0,0))
        pg.draw.rect(self.bboxsurf, (255,0,0, 255), self.bboxrect, width=1)

        self.cansurf = pg.image.load('./resources/can.png').convert_alpha()
        # self.cansurf = pg.transform.scale(self.cansurf, (w, h))
        self.canrect = self.cansurf.get_rect(topleft = (10, 10))



    def blit(self, window, topleft=(0,0)):
        window.blit(self.bboxsurf, topleft)
        window.blit(self.cansurf, self.canrect.topleft+topleft)


# class Inventory(pg.sprite.Sprite):

#     def __init__(self):


#         self.can = Can(10,10,64, 64)