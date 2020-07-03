from typing import List

import pygame

from object.base.moveable_object import MovableObject
from object.goal import Goal
from object.paddle import Paddle
from object.wall import Wall


class Ball(MovableObject):
    def __init__(self, surface: pygame.Surface, start_x: int, start_y: int, dx: int, dy: int, radius: int,
                 color: pygame.Color):
        super().__init__(surface, start_x, start_y, dx, dy, color)
        self._radius = radius

        # TODO: really shouldn't be a draw here
        self.rect = pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, val: int):
        self._radius = val

    def draw(self):
        self.rect = pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def update(self, collision_objects: List = None):
        collided_object = None
        if collision_objects:
            for obj in collision_objects:  # If the ball hits anything, flip the ball's direction
                check_rect = obj.rect
                if self.rect and check_rect and self.rect.colliderect(check_rect):
                    if type(obj) == Goal:
                        pass
                    elif type(obj) == Wall:
                        if obj.name == 'right' or obj.name == 'left':
                            self.dx = -self.dx
                        elif obj.name == 'top' or obj.name == 'bottom':
                            self.dy = -self.dy
                        else:
                            raise NotImplementedError
                    elif type(obj) == Paddle:
                        self.dx = -self.dx
                        self.dy = -self.dy + obj.dy
                    else:
                        raise NotImplementedError
                    collided_object = obj
                    break
        super().update()
        return collided_object
