import constants
import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
