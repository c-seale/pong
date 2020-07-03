import pygame

from object.base.moveable_object import MovableObject
from object.wall import Wall
from typing import List, Optional


class Paddle(MovableObject):
    def __init__(self, surface: pygame.Surface, start_x: int, start_y: int, dy: int, width: int, height: int,
                 color: pygame.Color):
        super().__init__(surface, start_x, start_y, self.dx, dy, color)
        self._width = width
        self._height = height

        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    @property
    def dx(self) -> int:
        return 0

    @dx.setter
    def dx(self, val: int):
        raise NotImplementedError

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def draw(self):
        self.rect = pygame.draw.rect(self.surface, self.color, self.rect)

    def update(self, arena_walls: List[Wall]) -> Optional[Wall]:
        collided_object = None

        # Figure out where the paddle is trying to move
        future_position = self.rect.move(0, self.dy)

        # If the target paddle destination does not collide, move it
        for wall in arena_walls:
            if future_position.colliderect(wall.rect):
                self.dy = 0
                collided_object = wall
                break
        if not collided_object:
            self.rect.y = future_position.y

        super().update()

        return collided_object
