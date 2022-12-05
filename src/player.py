import pygame

pygame.init()


class Player:
  
  def __init__ (self,x,y, win):
    self.rect = pygame.Rect(x,y, 32, 32)
    self.x = int(x)
    self.y = int(y)
    self.color = (255,0,0)
    self.velx = 0
    self.vely = 0
    self.leftPressed = False
    self.rightPressed = False
    self.upPressed = False
    self.downPressed = False
    self.speed = 2
    self.image = pygame.image.load("assets/boy.png")
    self.tridentState = "ready"
  
  def draw (self,win):
    # pygame.draw.rect(win,self.color, self.rect)
    win.blit(self.image, (self.x, self.y))
    

  def update(self):
    self.velx = 0
    self.vely = 0
    if self.leftPressed and not self.rightPressed:
      self.velx = -self.speed
    if self.rightPressed and not self.leftPressed:
      self.velx = self.speed
    if self.upPressed and not self.downPressed:
      self.vely = -self.speed
    if self.downPressed and not self.upPressed:
      self.vely = self.speed

    self.x += self.velx
    self.y += self.vely

    self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    #def throwTrident():
        
        # Creating a rectangle a distance away from the player based on accumulation value from some event hold (i.e. holding spacebar)
        # Runs a check to ensure the rectangle is lands in the water
        # Draw a small white circle at the rectangles center
        # Draw a black line back to top of player
        # If
