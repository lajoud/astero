from circleshape import CircleShape
from constants import *
from player import Player
from shot import Shot
import pygame
from logger import log_state, log_event


class Autoturret(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,AUTOTURRET_RADIUS)
        self.color="yellow"
        self.shot_timer=0
    
    
    def draw(self,screen,player):
        pygame.draw.circle(screen, self.color, player.position, self.radius,LINE_WIDTH)
    

    #the shoot function of the autoturret will shoot from the player center to the direction of any closeby asteroid
    #shooting speed is higher than the player
    #arguments are self, player (to get the position) and closeby asteroid to get the direction for the shot

    def update(self,dt,player,screen,asteroids):
        if self.shot_timer>0:
            self.shot_timer-=dt
        else:
            for element in asteroids:
                if pygame.math.Vector2.distance_to(player.position, element.position)<AUTOTURRET_DETECTION_AREA:
                    self.shot_timer=PLAYER_SHOOT_COOLDOWN_SECONDS*0.5
                    self.shoot(player,element)
                    break


    def shoot(self,player,asteroid):
        new_shot = Shot(player.position[0], player.position[1])
        shot_dir=pygame.Vector2(0,1).angle_to(asteroid.position-player.position)
        print(shot_dir)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(shot_dir) * PLAYER_SHOOT_SPEED*2

        """    
        new_shot = Shot(self.position[0], self.position[1])
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        """