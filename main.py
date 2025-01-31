import pygame  # noqa: F401
from constants import *  # noqa: F403
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock() # Create a clock object
    dt = 0 # Set the delta time to 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


    while True:
        for event in pygame.event.get(): # Get all the events that have happened
            if event.type == pygame.QUIT: # If the event is a quit event
                return
        
        for item in updatable:
            item.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.did_collide(asteroid):
                print("Game Over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.did_collide(asteroid):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0)) # Fill the screen with black

        for item in drawable:
            item.draw(screen)

        pygame.display.flip() # Update the screen

        # limit the frame rate to 60 fps and get the delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
