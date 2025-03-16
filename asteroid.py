import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, ASTEROID_MIN_RADIUS)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "White", (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        asteroid2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
        asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2