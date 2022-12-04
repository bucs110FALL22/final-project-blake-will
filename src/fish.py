import random
import pygame
pygame.init()

class Fish:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.value = 0
        self.speed = random.randrange(5, 10)
        if self.x == 800:
            self.speed * -1
        self.image = self.chooseFish()

    def chooseFish(self):
        type = random.randrange(101)
        if type > 0 and type <= 50:
            self.value = 10
            return pygame.image.load("assets/guppy.png")
        if type > 50 and type <= 70:
            self.value = 20
            return pygame.image.load("assets/bloob.png")
        if type > 70 and type <= 85:
            self.value = 35
            return pygame.image.load("assets/clownfish.png")
        if type > 85 and type <= 95:
            self.value = 50
            return pygame.image.load("assets/yellow.png")
        if type > 95 and type <= 100:
            self.value = 100
            return pygame.image.load("assets/shark.png")

    def reportValue(self):
        return self.value()

    def draw (self,win):
    # pygame.draw.rect(win,self.color, self.rect)
      win.blit(self.image, (self.x, self.y))
