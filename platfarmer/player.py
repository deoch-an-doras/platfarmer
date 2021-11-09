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
        self.friction = -0.15

        self.rect = self.surf.get_rect(center = self.pos)
        self.jumping = False
        self.scrolling_left = False
        self.scrolling_right = False

    def jump(self):

        if self.vel.y > -1:
            self.vel.y -= 15
        self.jumping= False


    def move(self):
    
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

    def scroll(self):
        if self.collisions:
            if self.scrolling_left:
                self.acc.x = -self.acc_rate
            if self.scrolling_right:
                self.acc.x = self.acc_rate
            if self.scrolling_right and self.scrolling_left:
                self.acc.x = 0
    

    def edge_case(self):

        if self.pos.x >= cst.WIDTH - self.width/2:
            self.pos.x = cst.WIDTH - self.width/2
            self.vel.x = -self.vel.x

        if self.pos.x <= self.width/2:
            self.pos.x = self.width/2
            self.vel.x = -self.vel.x

    def update(self, platforms):
        self.acc = vec(0,cst.GRAVITY)

        self.check_collide(platforms)

        if self.scrolling_left or self.scrolling_right:
            self.scroll()

        if self.jumping:
            self.jump()

        if self.collisions:
            self.acc.x += self.vel.x * self.friction

        self.edge_case()


        self.move()

    def check_collide(self, platforms):
        self.collisions = pg.sprite.spritecollide(self , platforms, False)
        if self.collisions:
            self.pos.y = self.collisions[0].rect.top -self.height/2
            self.vel.y = 0