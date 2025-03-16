import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                return
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision_check(asteroid):
                    # Handle collision (remove asteroid, split it, etc.)
                    asteroid.split()
                    shot.kill()
                    pass
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()