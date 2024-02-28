from typing import Any
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.car_1 = pygame.image.load('images/carBlue1.png').convert_alpha()
        self.car_2 = pygame.image.load('images/carBlue2.png').convert_alpha()
        self.car = [self.car_1, self.car_2]
        self.car_index = 0
        self.image = pygame.transform.scale(self.car[self.car_index], (44, 100))
        self.rect = self.image.get_rect(midbottom = (300, 550))

    def move_car_on_x_coordinate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.center[0] >= 124:
            self.rect.x -= 2
        if keys[pygame.K_d] and self.rect.center[0] <= 476:
            self.rect.x += 2
        if keys[pygame.K_p]:
            print(self.rect.center)

    def car_animation(self):
        self.car_index += 0.1
        if self.car_index >= 2:
            self.car_index = 0
        self.image = pygame.transform.scale(self.car[int(self.car_index)], (50, 100))

    def update(self):
        self.move_car_on_x_coordinate()
        self.car_animation()