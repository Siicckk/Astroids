import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"green", pygame.math.Vector2(self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity_top = self.velocity.rotate(random_angle) * 1.2
            velocity_bottom = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(*self.position, new_radius)
            asteroid_a.velocity = velocity_top
            asteroid_b = Asteroid(*self.position, new_radius)
            asteroid_b.velocity = velocity_bottom
            return asteroid_a, asteroid_b
