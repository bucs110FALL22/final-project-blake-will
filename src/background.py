import pygame
import random

pygame.init()


class Background:

    def __init__(self):
        self.image = pygame.image.load("assets/beech.jpg")
        self.yRange = 200
        
        self.screen = pygame.display.set_mode((600,400))
        self.showImage(self.screen)

    def spawn():
        side = random.randrange(0, 2, 1)
        if side == 0:
            pass
            # runs code to spawn fish on left side
        if side == 1:
            pass
            # runs code to spawn fish on right side

    def limit(self):
        return self.yRange


    def showImage(self, screen):
      screen.fill("white")
      pygame.display.flip()
      pygame.time.wait(1000)
      self.image.blit(screen, (0,0))
      pygame.display.flip()
      pygame.time.wait(2000)

fishing = Background()