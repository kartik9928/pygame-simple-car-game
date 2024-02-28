from typing import Any
import pygame

class Road(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.play_road = pygame.image.load('images/road.png').convert()
        self.image = pygame.transform.scale(self.play_road, (600, 600))
        self.rect = self.image.get_rect(topleft = (0, 0))

    def update(self):
        self.rect.y += 2
        pos = self.rect.y
        return pos