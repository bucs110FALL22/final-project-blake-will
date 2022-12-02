import pygame
import random
pygame.init()

class Background:
  def __init__(self):
    self.image = "image"
    self.yRange = 200

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