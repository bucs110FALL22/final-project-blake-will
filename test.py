import pygame
pygame.init()

def yellow():
  return ("yellow")

def main():
  screen = pygame.display.set_mode((600,400))
  fontStart = pygame.font.Font(None, 70)
  fontTitle = pygame.font.Font(None, 100)
  rectStartButton = ((200, 250), (200, 75))
  startHitbox = pygame.Rect(rectStartButton)
  screen.fill("white")
  pygame.draw.rect(screen, "palevioletred", rectStartButton)
  msgStart = fontStart.render("START", True, "black")
  msgTitle = fontTitle.render("Fishing  Game", True, "blue")
  screen.blit(msgStart, (220, 265))
  screen.blit(msgTitle, (65, 35))
  pygame.display.flip()
  run = True
  while run:
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
              clickPos = event.pos
              if startHitbox.collidepoint(clickPos):
                  screen.fill("white")
                  pygame.display.flip()
                  pygame.draw.rect(screen, "green", rectStartButton)
                  screen.blit(msgStart, (220, 265))
                  pygame.display.flip()
                  pygame.time.wait(350)
                  run = False
  print("Hello")


main()