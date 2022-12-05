import pygame
pygame.init()

class Trident:
  def __init__(self):

    self.image = pygame.image.load("assets/trident.png")
    self.x = 700
    self.y = 450
    self.changeX = 0
    self.changeY = -10
    #self.rect = self.image.get_rect()
    self.state = "ready"


  
  def throw(self, win, x, y):
    
    self.x = x
    self.y = y
    win.blit(self.image, (x, y))
    self.state = "fire"

  def update(self):
    if self.y < 0:
      self.x = 700
      self.y = 450
      self.state = "ready"
    if self.state == "fire":
      self.y += self.changeY
    self.rect = self.image.get_rect()
      
  def draw(self, win):
    win.blit(self.image, (self.x, self.y))
    
      
      
# def main():
#   trident = Trident()
#   print(trident.rect)

# main()