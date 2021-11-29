import sys
import random
import pygame as pg



import constants as cst

from plat import  Platform
from player import Player
from field import Field
from camera import Camera
from can import Can
from flower import Flower
from inventory import InventoryDisplay

pg.init()
pg.display.set_caption('Platfarmer')

FLOOR = (200, 0, 400, 20)

INIT_PLATS = [#( x ,  y ,  w ,   h)
                (210, 110, 90, 20),
                (270, 220, 70, 20),
                (100, 290, 50, 20), 
                (200, 350, 100, 20),                
                ]

CANS = [(120, 30),
         (280, 350)]

class Platfarmer:

    def __init__(self):

        self.running = True
        self.height, self.width = self.size = cst.SIZE

        self.clock = pg.time.Clock()
        self.fps = cst.FPS
        self.window = pg.display.set_mode(self.size)
        self.bgcolour = cst.BGCOLOUR

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.cans = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.fields = pg.sprite.Group()
        self.flowers = pg.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.camera = Camera(self.size)
        self.inventorydisplay = InventoryDisplay()  

        self.init_platforms()


    def init_platforms(self):
        floor = Platform(*FLOOR, False)
        self.add_sprite(floor,self.platforms)
        for plat in INIT_PLATS:
            self.add_sprite(Platform(*plat), self.platforms)
        
        self.highest_level = min([p.rect.top for p in self.platforms]) -self.height

        for can in CANS:
            self.add_sprite(Can(*can), self.cans)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.quit()
                elif event.key in (pg.K_UP, pg.K_w):
                    self.player.jumping = True
                elif event.key in (pg.K_LEFT, pg.K_a):
                    self.player.scrolling[0] = True
                elif event.key in (pg.K_RIGHT, pg.K_d):
                    self.player.scrolling[1] = True
                elif event.key in (pg.K_DOWN, pg.K_s):
                    self.player.ducking = True
                elif event.key == pg.K_SPACE:
                    self.player.watering = True

            elif event.type == pg.KEYUP:
                if event.key in (pg.K_LEFT, pg.K_a):
                    self.player.scrolling[0] = False
                elif event.key in (pg.K_RIGHT, pg.K_d):
                    self.player.scrolling[1] = False
                elif event.key in (pg.K_UP, pg.K_w):
                    self.player.jumping = False
                elif event.key in (pg.K_DOWN, pg.K_s):
                    self.player.ducking=False
                elif event.key == pg.K_SPACE:
                    self.player.watering = False

                                 
    def update(self):
        self.update_player()
        self.update_fields()
        self.update_platforms()
        self.update_cans()
        self.update_flowers()
        self.update_camera()
        self.update_inventory()


    def update_cans(self):
        for can in self.cans:
            can.update(self.player)

    def update_camera(self):
        self.camera.update(self.player.pos)

        self.spawn_new_platform()


    def update_flowers(self):
        pass

    def update_player(self):
        self.player.collisions = pg.sprite.spritecollide(self.player, self.all_sprites, False)
        self.player.platform_collisions = [s for s in self.player.collisions if isinstance(s, Platform)]
        self.player.field_collisions = [s for s in self.player.collisions if isinstance(s, Field)]
        self.player.update()

    def update_fields(self):
        
        for field in self.fields:
            field.update(self.player)

    def update_platforms(self):
        for platform in self.platforms:
            platform.update(self.player)
            if platform.needs_field:
                self.add_new_field(platform)


    def add_new_field(self, platform):
        self.add_sprite(Field(platform), self.fields)
        platform.needs_field = False
        platform.field_exists = True

    def update_inventory(self):
        self.inventorydisplay.update(self.player)

    def spawn_new_platform(self):

        if abs(self.camera.pos.y) > abs(self.highest_level)-self.height:
            w = random.randint(int(self.width/8),int(self.width/2))
            x = random.randint(0,self.width-w)
            y = random.randint(abs(self.highest_level)+30, abs(self.highest_level)+300)
            self.add_sprite(Platform(x,y,w,20), self.platforms)
            self.highest_level = y
            if random.random() <0.1:
                self.add_sprite(Can(x, y+40), self.cans)
            if random.random() <0.9:
                self.add_sprite(Flower(x, y+10), self.flowers)



    def add_sprites(self, sprites, group):
        for sprite in sprites:
            self.add_sprite(sprite, group)

    def add_sprite(self, sprite, group):
        group.add(sprite)
        self.all_sprites.add(sprite)

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
            self.window.blit(sprite.surf, self.camera.translate(sprite))
        self.window.blit(self.player.surf, self.camera.translate(self.player))
        self.inventorydisplay.blit(self.window)

    def quit(self):
        pg.quit()
        sys.exit()

g = Platfarmer()
g.mainloop()
