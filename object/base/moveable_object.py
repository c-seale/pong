from typing import List

import pygame

from object.base.object import ObjectBase


class MovableObject(ObjectBase):
    def __init__(self, screen: pygame.Surface, start_x: int, start_y: int, dx: int, dy: int, color: pygame.Color):
        super().__init__(screen, start_x, start_y, color)
        self._dx = dx
        self._dy = dy

    @property
    def dx(self) -> int:
        return self._dx

    @dx.setter
    def dx(self, val: int):
        self._dx = val

    @property
    def dy(self) -> int:
        return self._dy

    @dy.setter
    def dy(self, val: int):
        self._dy = val

    def draw(self):
        raise NotImplementedError

    def update(self, **kwargs):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.draw()
