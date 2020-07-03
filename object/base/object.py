from typing import Optional

import pygame


class ObjectBase:
    def __init__(self, surface: pygame.Surface, x: int, y: int, color: pygame.Color):
        self._surface = surface
        self._x = x
        self._y = y
        self._color = color
        self._rect = None

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

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

    def draw(self):
        raise NotImplementedError
