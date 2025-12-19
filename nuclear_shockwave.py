from circleshape import CircleShape
from constants import *
import pygame
import math


class Nuclear_shockwave(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__( x, y,radius)
        self.color="green"
        self.timer=0



    def update(self,dt):
        self.radius *= 1.005
        self.timer+=dt
        if self.radius>ASTEROID_MIN_RADIUS*10:
            self.kill()

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius,LINE_WIDTH)