from snake import SnakeClass
from food import FoodClass
import config
import random
import pygame
pygame.init()

screen = pygame.display.set_mode((config.width,config.height))

s = SnakeClass()

clock = pygame.time.Clock()

food = FoodClass()

score = 0

def key_pressed():
    if  event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            s.dir(0, -1)
        elif event.key == pygame.K_DOWN:
            s.dir(0, 1)
        elif event.key == pygame.K_RIGHT:
            s.dir(1, 0)
        elif event.key == pygame.K_LEFT:
            s.dir(-1, 0)


running = True
while running:
    # This controls the framerate
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    key_pressed()

    if s.eat(food):
        food.pick_location()
        score += 1
        print("Score:",score)

    s.update()
    s.show(screen)

    if s.death():
        print("Game Over")
        running = False

    food.show(screen)

    pygame.display.update()
