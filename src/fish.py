import random
import pygame
pygame.init()

class Fish:

    def __init__(self, x, y):
        super().__init__()
      
        self.x = int(x)
        self.y = int(y)
        self.value = 0
        self.speed = 5
        self.image = pygame.image.load("assets/guppy.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("assets/guppy.png")
        type = random.randrange(101)
        if type > 0 and type <= 50:
            self.value = 10
            self.speed = 3
            self.image = pygame.image.load("assets/guppy.png")
        if type > 50 and type <= 70:
            self.value = 20
            self.speed = 4
            self.image = pygame.image.load("assets/bloob.png")
        if type > 70 and type <= 85:
            self.value = 35
            self.speed = 6
            self.image = pygame.image.load("assets/clownfish.png")
        if type > 85 and type <= 95:
            self.value = 50
            self.speed = 8
            self.image = pygame.image.load("assets/yellow.png")
        if type > 95 and type <= 100:
            self.value = 100
            self.speed = 10
            self.image = pygame.image.load("assets/shark.png")

    # def chooseFish(self):
    #     type = random.randrange(101)
    #     if type > 0 and type <= 50:
    #         self.value = 10
    #         self.speed = 3
    #         return pygame.image.load("assets/guppy.png")
    #     if type > 50 and type <= 70:
    #         self.value = 20
    #         self.speed = 4
    #         return pygame.image.load("assets/bloob.png")
    #     if type > 70 and type <= 85:
    #         pass
    #         # self.value = 35
    #         # self.speed = 6
    #         # return pygame.image.load("assets/clownfish.png")
    #     if type > 85 and type <= 95:
    #         self.value = 50
    #         self.speed = 8
    #         return pygame.image.load("assets/yellow.png")
    #     if type > 95 and type <= 100:
    #         self.value = 100
    #         self.speed = 10
    #         return pygame.image.load("assets/shark.png")

    def update(self):
      if self.x < 0:
        self.x = 0
        self.speed = self.speed * -1
      if self.x > 800:
        self.x = 800
        self.speed = self.speed * -1
      self.x += self.speed
      self.rect = self.image.get_rect()

        
        

    def reportValue(self):
        return self.value()

    def draw (self,win):
    # pygame.draw.rect(win,self.color, self.rect)
      win.blit(self.image, (self.x, self.y))
