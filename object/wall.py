import pygame

from object.base.object import ObjectBase


class Wall(ObjectBase):
    def __init__(self, name: str, screen: pygame.Surface, top_left_x: int, top_left_y: int, width: int, height: int,
                 color: pygame.Color):
        super().__init__(screen, top_left_x, top_left_y, color)
        self._width = width
        self._height = height
        self._name = name

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def name(self) -> str:
        return self._name.lower()

    def draw(self):
        self.rect = pygame.draw.rect(self.surface, self.color, pygame.Rect((self.x, self.y), (self.width, self.height)))
