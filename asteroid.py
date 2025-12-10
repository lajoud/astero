from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        self.attributes=""
        rand_attributes =random.random()
        rand_attributes_types=random.uniform(0,2)
        
        if 0<rand_attributes<0.1:
            if 0<=rand_attributes_types<1:
                self.color="yellow"
                self.attributes="autoturret"
            elif 1<=rand_attributes_types<=2:
                self.color="purple"
                self.attributes="machine_gun"
        else:
            self.color="white"


    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius,LINE_WIDTH)
    
    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            temp_angle=random.uniform(20,50)
            new_dir1=self.velocity.rotate(temp_angle)
            new_dir2=self.velocity.rotate(-temp_angle)
            new_radius=self.radius-ASTEROID_MIN_RADIUS

            new_asteroid1=Asteroid(self.position[0],self.position[1],new_radius)
            new_asteroid1.velocity=new_dir1*1.2
            new_asteroid2=Asteroid(self.position[0],self.position[1],new_radius)
            new_asteroid2.velocity=new_dir2*1.2
