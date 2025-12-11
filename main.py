import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from upgrade import Autoturret
#from upgrade import Shield
import sys

def main():
    pygame.init()
    my_clock=pygame.time.Clock()
    dt=0


    updatable = pygame.sprite.Group()
    drawable =pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots= pygame.sprite.Group()
    

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers=(shots,updatable,drawable)
    #Autoturret.Containers=(drawable)
    #Shield.containers=(updatable,drawable)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    new_player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    my_asteroid_field=AsteroidField()
    autoturret=Autoturret(new_player.position[0],new_player.position[1])
    
    new_score=0
    shield_limit=0
    shield_bucket=0
    life_bucket=0
    life_count=0

    print("starting game loop")
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        #update on the autoturret
        if new_player.attribute=="autoturret":
            autoturret.update(dt,new_player,screen,asteroids)

        for element in asteroids:
            if element.collides_with(new_player):
                if new_player.shield_power_up==True:
                    element.kill()
                    new_player.shield_power_up=False
                    log_event("Shield OFF")
                elif life_count>0:
                    element.kill()
                    life_count -= 1
                    log_event("One less Life")
                else:
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()

        for element in drawable:
            element.draw(screen)
        
        #draw autoturret here, does not have the save draw method argument
        if new_player.attribute=="autoturret":
            autoturret.draw(screen,new_player,)

            
        


        for element in asteroids:
            for bullet in shots:
                if element.collides_with(bullet):
                    log_event("asteroid_shot")
                    if element.attributes=="machine_gun":
                        new_player.attribute="machine_gun"
                        log_event("machine gun mode ON")
                        new_player.attribute_timer=4
                    elif element.attributes=="autoturret":
                        new_player.attribute="autoturret"
                        log_event("autoturret mode ON")
                        new_player.attribute_timer=6
                    bullet.kill()
                    element.split()
                    new_score += 300*ASTEROID_MIN_RADIUS/element.radius

                    shield_bucket+=300*ASTEROID_MIN_RADIUS/element.radius
                    if shield_bucket>=  SHIELD_POWER_UP:
                       new_player.shield_power_up=True
                       shield_bucket=0 #reset of the bucket
                       log_event("Shield ON")
                    
                    life_bucket += 300*ASTEROID_MIN_RADIUS/element.radius
                    if life_bucket>=  LIFE_UP:
                       life_count += 1
                       life_bucket=0 #reset of the life bucket
                       log_event("One more life")

        pygame.display.flip()
        
        dt =my_clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
