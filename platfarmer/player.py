import pygame as pg
import constants as cst


vec = pg.math.Vector2  # 2 for two dimensional


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height, self.width = self.size = (30, 30)
        self.color = (128, 255, 40)
        
        self.pos = vec((15, 400))
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
    
        self.surf = pg.Surface(self.size)
        self.surf.fill(self.color)

        self.acc_rate = 0.5

        self.rect = self.surf.get_rect(center = self.pos)
        self.jumping = False
        self.ducking = False
        self.scrolling = [False, False]
        self.watering = False

        self.water = 2000

        self.platform_collisions = []
        self.field_collisions = []

    def jump(self):

        if self.vel.y > -1:
            self.vel.y = -15
        self.jumping= False

    def move(self):
    
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

    def scroll(self):
        if self.platform_collisions:
            if self.scrolling[0] :
                self.acc.x = -self.acc_rate
            if self.scrolling[1]:
                self.acc.x = self.acc_rate
            if all(self.scrolling):
                self.acc.x = 0   

    def update(self):
        self.acc = vec(0,cst.GRAVITY)

        self.platform_interactions()
        self.field_interactions()

        if any(self.scrolling):
            self.scroll()

        if self.jumping:
            self.jump()

        self.edge_case()

        self.move()

    def platform_interactions(self):

        if self.platform_collisions:
            platform = self.platform_collisions[0]
            if self.vel.y > 0:
                if not (platform.duckable and (self.ducking or platform.being_ducked)):
                    self.pos.y = platform.rect.top-self.height/2
                    self.vel.y = 0
            self.acc.x += self.vel.x * platform.friction
        

    def field_interactions(self):
        if self.field_collisions:
            field = self.field_collisions[0]
            if self.watering and self.water > 0:
                field.being_watered = True
                self.water -= 10

    def edge_case(self):

        if self.pos.x >= cst.WIDTH - self.width/2:
            self.pos.x = cst.WIDTH - self.width/2
            self.vel.x = -self.vel.x

        if self.pos.x <= self.width/2:
            self.pos.x = self.width/2
            self.vel.x = -self.vel.x