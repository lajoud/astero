import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from upgrade import Autoturret
#from upgrade import Shield
from score_sheet import score_sheet_edition
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

    white=(255,255,255)
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 28)

    # create a text surface object,
    # on which text is drawn on it.
    text1 = font.render('Score: 0', True, white)
    # create a rectangular object for the
    # text surface object
    textRect1 = text1.get_rect()
    #set the center of the rectangular object.
    textRect1.center = (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10)

    # create a text surface object,
    # on which text is drawn on it.
    text2 = font.render('Life: 0', True, white)
    # create a rectangular object for the
    # text surface object
    textRect2 = text2.get_rect()
    #set the center of the rectangular object.
    textRect2.center = (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5)



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
                    score_history=score_sheet_edition(new_score)
                    log_event("player_hit")
                    log_event("Game over!")
                    print("Game Over")
                    sys.exit()

        for element in drawable:
            element.draw(screen)
        
        #draw autoturret here, does not have the save draw method argument
        if new_player.attribute=="autoturret":
            autoturret.draw(screen,new_player,)

            
        
        for element in asteroids:
            for bullet in shots:
                if element.collides_with(bullet):
                    #update score and shield bucket
                    new_score += 300*ASTEROID_MIN_RADIUS/element.radius
                    shield_bucket+=300*ASTEROID_MIN_RADIUS/element.radius

                    log_event("asteroid_shot")
                    if element.attributes=="machine_gun":
                        new_player.attribute="machine_gun"
                        log_event("machine gun mode ON")
                        new_player.attribute_timer=4
                        bullet.kill()
                        element.split()
                    elif element.attributes=="autoturret":
                        new_player.attribute="autoturret"
                        log_event("autoturret mode ON")
                        new_player.attribute_timer=6
                        bullet.kill()
                        element.split()
                    elif element.attributes=="explosion":
                        log_event("Explosion occurs")
                        element.explode()
                    else:
                        bullet.kill()
                        element.split()

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
        text1 = font.render(f"Score: {new_score}", True, white)
        # text1=f"Score:{new_score}"
        text2 = font.render(f"Life: {life_count}", True, white)
        #text2=f"Life: {life_count}"
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        pygame.display.update()

        dt =my_clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
