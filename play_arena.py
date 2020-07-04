from typing import List

import pygame

from object.goal import Goal
from object.wall import Wall


class PlayArena:
    def __init__(self, surface: pygame.Surface, background_color: pygame.Color, wall_size: int,
                 wall_color: pygame.Color):
        self._surface = surface
        self._background_color = background_color
        self._wall_size = wall_size
        self._wall_color = wall_color

        # walls
        self._wall_top = Wall('top', self.surface, 0, 0, self.surface.get_width(), self.wall_size * 4, self.wall_color)
        self._wall_bottom = Wall('bottom', self.surface, 0, self.surface.get_height() - self.wall_size,
                                 self.surface.get_width(), self.wall_size, self.wall_color)

        # goals
        self._goal_left = Goal('left', self.surface, 0, 0, 0, self.surface.get_height(), self.background_color)
        self._goal_right = Goal('right', self.surface, self.surface.get_width(), 0, 0, self.surface.get_height(),
                                self.wall_color)

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    @property
    def background_color(self) -> pygame.Color:
        return self._background_color

    @property
    def wall_size(self) -> int:
        return self._wall_size

    @property
    def wall_color(self) -> pygame.Color:
        return self._wall_color

    @property
    def walls(self) -> List[Wall]:
        return [self.wall_top, self.wall_bottom]

    @property
    def wall_top(self) -> Wall:
        return self._wall_top

    @property
    def wall_bottom(self) -> Wall:
        return self._wall_bottom

    @property
    def goals(self) -> List[Goal]:
        return [self.goal_left, self.goal_right]

    @property
    def goal_left(self) -> Goal:
        return self._goal_left

    @property
    def goal_right(self) -> Goal:
        return self._goal_right

    def render_background(self):
        self.surface.fill(self.background_color)

    def render_boundaries(self):
        for goal in self.goals:
            goal.draw()
        for wall in self.walls:
            wall.draw()

    def render_scoreboard(self, player_one_score: int, player_two_score: int):
        font = pygame.font.SysFont(pygame.font.get_default_font(),
                                   int(1250 * self.wall_top.height / self.surface.get_height()))
        p1_score = font.render('{}'.format(player_one_score), True, (255, 255, 255))
        p2_score = font.render('{}'.format(player_two_score), True, (255, 255, 255))

        self.surface.blit(p1_score, (self.surface.get_width() * 0.25, 0))
        self.surface.blit(p2_score, (self.surface.get_width() * 0.75, 0))

    def render_divider(self):
        pygame.draw.line(self.surface, pygame.Color('gray'), (self.surface.get_width() / 2, 0),
                         (self.surface.get_width() / 2, self.surface.get_height()), round(self.wall_size * 0.3))

    def update(self, player_one_score: int, player_two_score: int):
        self.render_background()
        self.render_divider()
        self.render_boundaries()
        self.render_scoreboard(player_one_score, player_two_score)
