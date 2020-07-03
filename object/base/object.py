from typing import Optional

import pygame


class ObjectBase:
    def __init__(self, surface: pygame.Surface, x: int, y: int, color: pygame.Color):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.rect = None

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    @surface.setter
    def surface(self, val: pygame.Surface):
        self._surface = val

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, val: int):
        self._x = val

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

    @property
    def rect(self) -> Optional[pygame.Rect]:
        return self._rect

    @rect.setter
    def rect(self, val: pygame.Rect):
        self._rect = val

    @property
    def color(self) -> pygame.Color:
        return self._color

    @color.setter
    def color(self, val: pygame.Color):
        self._color = val

    def draw(self):
        raise NotImplementedError
