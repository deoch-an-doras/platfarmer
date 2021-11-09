import sys
import pygame as pg

import constants as cst

from platform import  Platform
from player import Player

pg.init()
pg.display.set_caption('Game')

class Game:

    

    def __init__(self):

        self.running = True
        self.height, self.width = self.size = cst.SIZE

        self.clock = pg.time.Clock()
        self.fps = 60
        self.window = pg.display.set_mode(self.size)

        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)
        for pos in [(200, 440, 400, 20), (200, 300, 100, 20)]:
            print(pos)
            platform = Platform(*pos)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.quit()
                elif event.key == pg.K_UP:
                    self.player.jumping = True
                elif event.key == pg.K_LEFT:
                    self.player.scrolling_left = True
                elif event.key == pg.K_RIGHT:
                    self.player.scrolling_right = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.player.scrolling_left = False
                elif event.key == pg.K_RIGHT:
                    self.player.scrolling_right = False
                
    def update(self):
        self.player.update(self.platforms)



    def draw(self):
        self.window.fill((255,255,255))
        for sprite in self.all_sprites:
            self.window.blit(sprite.surf, sprite.rect)

    def quit(self):
        pg.quit()
        sys.exit()

    def mainloop(self):

        while self.running:

            self.events()
            self.update()
            self.draw()
    
            pg.display.update()
            self.clock.tick(self.fps)

 

g = Game()

g.mainloop()
