import sys
import pygame as pg

import constants as cst

from plat import  Platform
from player import Player
from field import Field
from camera import Camera
from can import Can

pg.init()
pg.display.set_caption('Platfarmer')

FLOOR = (200, 0, 400, 20)

INIT_PLATS = [#( x ,  y ,  w ,   h)
                (210, 110, 90, 20),
                (270, 220, 70, 20),
                (100, 290, 50, 20), 
                (200, 350, 100, 20), 
                (120, 410, 40, 20),
                (25, 510, 45, 20),
                (100, 580, 90, 20),
                (90, 660, 120, 20),                
                ]

CANS = [(120, 30, 200, 200),
         (240, 320, 200, 200)]

class Platfarmer:

    def __init__(self):

        self.running = True
        self.height, self.width = self.size = cst.SIZE

        self.clock = pg.time.Clock()
        self.fps = 60
        self.window = pg.display.set_mode(self.size)

        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.fields = pg.sprite.Group()
        self.cans = pg.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.camera = Camera(self.size)
        self._platforms = []

        self.floor = pg.sprite.Group()

        self.init_platforms()


    def init_platforms(self):
        floor = Platform(*FLOOR, False)
        self.floor.add(floor)
        self.platforms.add(floor)
        self.all_sprites.add(floor)

        for plat in INIT_PLATS:
            platform = Platform(*plat)
            self.platforms.add(platform)
            self.all_sprites.add(platform)
        for can in CANS:
            can = Can(*can)
            self.cans.add(can)
            self.all_sprites.add(can)

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
                    self.player.scrolling[0] = True
                elif event.key == pg.K_RIGHT:
                    self.player.scrolling[1] = True
                elif event.key == pg.K_SPACE:
                    self.player.growing = True
                elif event.key == pg.K_DOWN:
                    self.player.ducking = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.player.scrolling[0] = False
                elif event.key == pg.K_RIGHT:
                    self.player.scrolling[1] = False
                elif event.key == pg.K_UP:
                    self.player.jumping = False
                elif event.key == pg.K_SPACE:
                    self.player.growing = False
                elif event.key == pg.K_DOWN:
                    self.player.ducking=False
                    
                
    def update(self):
        self.update_collisions()
        self.update_player()
        self.update_fields()
        self.update_platforms()
        self.update_camera()
        self.update_cans()

    def update_cans(self):
        pass


    def update_camera(self):
        self.camera.update(self.player.pos)

    def update_collisions(self):
        self.player.platform_collisions = pg.sprite.spritecollide(self.player, self.platforms, False)
        self.player.field_collisions = pg.sprite.spritecollide(self.player, self.fields, False)
        self.player.can_collisions = pg.sprite.spritecollide(self.player, self.fields, False)

    def update_player(self):
        self.player.update()

    def update_fields(self):
        if self.player.growing:
            if not self.player.field_collisions:
                if self.player.platform_collisions:
                    platform = self.player.platform_collisions[0]
                    field = Field(platform)
                    self.fields.add(field)
                    self.all_sprites.add(field)
            else:
                self.player.field_collisions[0].growing = True
        else:
            for field in self.fields: 
                field.growing = False

        for field in self.fields:
            field.update()

    def update_platforms(self):

        for platform in self.player.platform_collisions:
            if self.player.ducking and not platform.being_ducked:
                platform.duck_start = pg.time.get_ticks()
                platform.being_ducked = True
            platform.update()



    def mainloop(self):

        while self.running:

            self.events()
            self.update()
            self.draw()
    
            pg.display.update()
            self.clock.tick(self.fps)

    def draw(self):
        self.window.fill((255,255,255))
        for sprite in self.all_sprites:
            self.window.blit(sprite.surf, (sprite.rect.x, 
                        sprite.rect.y-self.camera.pos.y))
        self.window.blit(self.player.surf, (self.player.rect.x, 
                        self.player.rect.y-self.camera.pos.y))
        

    def quit(self):
        pg.quit()
        sys.exit()


g = Platfarmer()

g.mainloop()
