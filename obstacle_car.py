import pygame
from random import choice, randint, randrange, shuffle

class cars_creation(pygame.sprite.Sprite):

    def __init__(self, car_x_co, car_speed):
        super().__init__()
        self.car_speed = car_speed
        shuffle(car_x_co)
        self.car_x = choice(car_x_co)
        self.obstacle_1 = pygame.image.load('images/carRed1.png').convert_alpha()
        self.obstacle_2 = pygame.image.load('images/carRed2.png').convert_alpha()
        self.obstacle = [self.obstacle_1, self.obstacle_2]
        self.obstacle_index = 0
        self.image = pygame.transform.scale(self.obstacle[self.obstacle_index], (44, 100))
        self.rect = self.image.get_rect(midbottom = (self.car_x, -250 ))

    def destroy(self):
        if self.rect.top > 610:
            self.kill()

    def obstacle_animation(self):
        self.obstacle_index += 0.1
        if self.obstacle_index >= 2:
            self.obstacle_index = 0
        self.image = pygame.transform.scale(self.obstacle[int(self.obstacle_index)], (50, 100))


    def update(self, speed=10):
        self.rect.y += speed
        self.destroy()
        self.obstacle_animation()