from circleshape import CircleShape
from constants import LINE_WIDTH, SHIELD_RADIUS
from player import Player
import pygame
from logger import log_state, log_event


"""def autoturret_updgrade():
    continue

def machine_gun(player):
    player.sh
    
"""class Shield(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHIELD_RADIUS)
        self.rotation=0

    def draw(self,screen, player):
        pygame.draw.circle(screen, "blue", player.position, self.radius,LINE_WIDTH)
    
    def update(self,dt):
        self.position += self.velocity*dt
"""
   