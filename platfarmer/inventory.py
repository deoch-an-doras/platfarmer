import pygame as pg
import constants as cst


pg.font.init() # you have to call this at the start, 
                   # if you want to use this module.

class InventoryDisplay(pg.sprite.Sprite):

    def __init__(self, w=200, h=100):
        super().__init__()
        

        self.bboxsurf = pg.Surface((w, h)).convert_alpha()
        self.bboxsurf.fill((0,0,0,0))
        self.bboxrect = self.bboxsurf.get_rect(topleft = (0,0))
        pg.draw.rect(self.bboxsurf, (255,0,0, 255), self.bboxrect, width=1)

        self.cansurf = pg.image.load('./resources/can.png').convert_alpha()
        self.canrect = self.cansurf.get_rect(centery = self.bboxrect.centery, left = self.bboxrect.left+10)
        
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        
        self.textsurf = self.font.render('', False, (0, 0, 0))
        self.textrect = self.textsurf.get_rect(centery = self.bboxrect.centery, left = self.canrect.right+10)
    
    def update(self, player):
        waterstring = str(int(player.water/1000))
        self.textsurf = self.font.render(waterstring, False, (0, 0, 0))
        self.textrect = self.textsurf.get_rect(centery = self.bboxrect.centery, left = self.canrect.right+10)
    

    def blit(self, window, topleft=(0,0)):
        window.blit(self.bboxsurf, topleft)
        window.blit(self.cansurf, self.canrect.topleft+topleft)
        window.blit(self.textsurf, self.textrect.topleft+topleft)




# class Inventory(pg.sprite.Sprite):

#     def __init__(self):


#         self.can = Can(10,10,64, 64)