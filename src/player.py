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
    self.left_pressed = False
    self.right_pressed = False
    self.up_pressed = False
    self.down_pressed = False
    self.speed = 4
    self.image = pygame.image.load("assets/boy.png")
  def draw (self,win):
    # pygame.draw.rect(win,self.color, self.rect)
    win.blit(self.image, (self.x, self.y))
    

  def update(self):
    self.velx = 0
    self.vely = 0
    if self.left_pressed and not self.right_pressed:
      self.velx = -self.speed
    if self.right_pressed and not self.left_pressed:
      self.velx = self.speed
    if self.up_pressed and not self.down_pressed:
      self.vely = -self.speed
    if self.down_pressed and not self.up_pressed:
      self.vely = self.speed

    self.x += self.velx
    self.y += self.vely

    self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

# player = Player(width/2, height/2)

# while True:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       sys.exit()
#     if event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_LEFT:
#         player.left_pressed = True
#       if event.key == pygame.K_RIGHT:
#         player.right_pressed = True
#       if event.key == pygame.K_UP:
#         player.up_pressed = True
#       if event.key == pygame.K_DOWN:
#         player.down_pressed = True
#     if event.type == pygame.KEYUP:
#       if event.key == pygame.K_LEFT:
#         player.left_pressed = False
#       if event.key == pygame.K_RIGHT:
#         player.right_pressed = False
#       if event.key == pygame.K_UP:
#         player.up_pressed = False
#       if event.key == pygame.K_DOWN:
#         player.down_pressed = False

#   self.screen.fill((12,24,36))
#   player.draw(x, y, self.scren)

#   player.update()
#   pygame.display.flip()

#   clock.tick(120)

    def castHook():
        pass
        # Creating a rectangle a distance away from the player based on accumulation value from some event hold (i.e. holding spacebar)
        # Runs a check to ensure the rectangle is lands in the water
        # Draw a small white circle at the rectangles center
        # Draw a black line back to top of player
        # If
