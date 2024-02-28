import pygame
from random import randint
import math
from player_car import Player
from right_obstacle_car import Right_cars
from left_obstacle_car import Left_cars

def cars_collision():
    global high_score
    if pygame.sprite.spritecollide(player.sprite, right_car, False) or pygame.sprite.spritecollide(player.sprite, left_car, False):
        crash.play()
        traffi.stop()
        engine.stop()
        if int(current_score) > int(high_score):
            with open("score.txt", 'w') as file:
                file.write(str(current_score))
        return False
    else:
        return True

def score_board():
    global current_score
    time = pygame.time.get_ticks() - timer
    current_score = math.ceil(time / 1000)
    score = text.render(f'Score {current_score}', False, "#FFD500")
    score_rect = score.get_rect(topleft= (10, 10))
    screen.blit(score, score_rect)

def group_car_collide():
    collisions = pygame.sprite.groupcollide(right_car, right_car, False, False)
    for collided_cars in collisions.values():
        if len(collided_cars) > 1:
            for collided_car in collided_cars:
                right_car.remove(collided_car)


pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
text = pygame.font.Font(None, 30)

# variables
current_score = 0
high_score = 0
car_running = True
running = True
road_loop = 0
car_gear = 0
timer = 0

# high score
with open("score.txt", 'r') as file:
    high_score = file.readline()

# surface
play_road = pygame.image.load('images/road.png').convert()
play_road = pygame.transform.scale(play_road, (600, 600))

# player group
player = pygame.sprite.GroupSingle()
player.add(Player())

# obstacle group
right_car = pygame.sprite.Group()
left_car = pygame.sprite.Group()

# new user event
right_car_timer = pygame.USEREVENT + 1
pygame.time.set_timer(right_car_timer, randint(2500, 6000))

left_car_timer = pygame.USEREVENT + 2
pygame.time.set_timer(left_car_timer, 1000)


# game sound
music = pygame.mixer.Sound('./sound/bg-music.mp3')
music.set_volume(0.5)
music.play(loops = -1)

traffi = pygame.mixer.Sound('./sound/traffic.mp3')
traffi.set_volume(0.3)
traffi.play(loops = -1)

crash = pygame.mixer.Sound('./sound/car-crash.mp3')

engine = pygame.mixer.Sound('./sound/engine2.mp3')
engine_speed = 0.0
engine.set_volume(engine_speed)
engine.play(loops = -1)

while running:

    # player input event
    for event in pygame.event.get():
        # quit game event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # key down event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                traffi.play(loops = -1)
                engine.play(loops = -1)
                car_running = True
                right_car.empty()
                left_car.empty()
                timer = pygame.time.get_ticks()

        # car event
        if event.type == right_car_timer:
            right_car.add(Right_cars())
        if event.type == left_car_timer:
            left_car.add(Left_cars())

        # # car gear control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and car_gear < 5:
                car_gear += 1
                engine_speed = 0.1 * car_gear
                engine.set_volume(engine_speed)
            if event.key == pygame.K_s and car_gear > 0:
                car_gear -= 1
                engine_speed = 0.1 * car_gear
                engine.set_volume(engine_speed)

    if car_running:
        # game update
        screen.fill((0,0,0))
        screen.blit(play_road, (0, road_loop))
        screen.blit(play_road, (0, road_loop-600))
        if (road_loop >= 600):
            screen.blit(play_road, (0, road_loop-600))
            road_loop = 0
        road_loop += car_gear

        # sprite class update
        player.draw(screen)
        player.update()
        right_car.draw(screen)
        right_car.update(car_gear-1)
        left_car.draw(screen)
        left_car.update()

        # function call
        car_running = cars_collision()
        score_board()
        group_car_collide()

        collisions = pygame.sprite.groupcollide(right_car, right_car, False, False)
        for collided_cars in collisions.values():
            if len(collided_cars) > 1:
                for collided_car in collided_cars:
                    right_car.remove(collided_car)

    else:
        pass




    pygame.display.update()
    clock.tick(50)