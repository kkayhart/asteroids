import pygame
import constants
import random

from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        pos_angle = self.velocity.rotate(new_angle)
        neg_angle = self.velocity.rotate(-new_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        pos_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        pos_asteroid.velocity = pos_angle * 1.2
        neg_asteroid.velocity = neg_angle * 1.2
