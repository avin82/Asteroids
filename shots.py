import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "White", (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y