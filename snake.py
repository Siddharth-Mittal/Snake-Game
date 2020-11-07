import pygame
import config

class SnakeClass:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_speed = 1
        self.y_speed = 0
        self.tail = []


    def eat(self, other):
        dist = (((self.x-other.x)**2) + ((self.y-other.y)**2))**0.5
        if dist < 1:
            self.tail.append(pygame.Rect(self.x, self.y, (config.scale-1), (config.scale-1)))
            return True
        else:
            return False


    def dir(self, x, y):
        self.x_speed = x
        self.y_speed = y


    def death(self):
        for i in range(len(self.tail)):
            part_of_tail = self.tail[i]
            dist = (((self.x-part_of_tail.x)**2) + ((self.y-part_of_tail.y)**2))**0.5
            if dist < 1:
                self.tail = []
                print("Death")
                return True



    def update(self):

        # Updating Snake Tail Position
        for i in range(len(self.tail)-1):
            self.tail[i] = self.tail[i+1]
        if len(self.tail) != 0:
            self.tail[-1] = pygame.Rect(self.x, self.y, (config.scale-1), (config.scale-1))


        self.x += self.x_speed * config.scale
        self.y += self.y_speed * config.scale

        if self.x < 0:
            self.x = config.width - config.scale
        if self.x > (config.width-config.scale):
            self.x = 0
        if self.y < 0:
            self.y = config.height - config.scale
        if self.y > (config.height-config.scale):
            self.y = 0



    def show(self, surface):
        for i in range(len(self.tail)):
            pygame.draw.rect(surface, (255,0,0), self.tail[i])

        # pygame.draw.rect(surface, color, pygame Rect object )
        pygame.draw.rect(surface, (240,0,0), pygame.Rect(self.x, self.y, (config.scale-1), (config.scale-1)))
