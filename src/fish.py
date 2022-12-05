import random
import pygame
pygame.init()

class Fish:

    def __init__(self, x, y):
        super().__init__()
      
        self.x = int(x)
        self.y = int(y)
        self.value = 0
        self.speed = 0
        self.image = pygame.image.load("assets/guppy.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("assets/guppy.png")
        type = random.randrange(101)
        if type > 0 and type <= 50:
            self.value = 10
            self.speed = 0.8
            self.image = pygame.image.load("assets/guppy.png")
            self.image = pygame.transform.flip(self.image, True, False)
        if type > 50 and type <= 70:
            self.value = 20
            self.speed = 1
            self.image = pygame.image.load("assets/bloob.png")
            self.image = pygame.transform.flip(self.image, True, False)
        if type > 70 and type <= 85:
            self.value = 35
            self.speed = 1.5
            self.image = pygame.image.load("assets/clownfish.png")
            self.image = pygame.transform.flip(self.image, True, False)
        if type > 85 and type <= 95:
            self.value = 50
            self.speed = 2
            self.image = pygame.image.load("assets/yellow.png")
            self.image = pygame.transform.flip(self.image, True, False)
        if type > 95 and type <= 100:
            self.value = 100
            self.speed = 3
            self.image = pygame.image.load("assets/shark.png")
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
      if self.x < 0:
        self.x = 0
        self.speed = self.speed * -1
        self.image = pygame.transform.flip(self.image, True, False)
      if self.x > (800 - self.image.get_width()):
        self.x = (800 - self.image.get_width())
        self.speed = self.speed * -1
        self.image = pygame.transform.flip(self.image, True, False)
      self.x += self.speed
      self.rect = self.image.get_rect()

        
        

    def reportValue(self):
        return self.value()

    def draw (self,win):
    # pygame.draw.rect(win,self.color, self.rect)
      win.blit(self.image, (self.x, self.y))
