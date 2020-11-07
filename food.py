import pygame
import random
import config

class FoodClass:
    def __init__(self):
        FoodClass.pick_location(self)

    def pick_location(self):
        self.x = random.randrange(0,config.ws) * config.scale
        self.y = random.randrange(0,config.hs) * config.scale

    def show(self, surface):
        pygame.draw.rect(surface, (0,255,255), pygame.Rect(self.x, self.y, config.scale, config.scale))
