import pygame
from src.background import Background
from src.fish import Fish
from src.player import Player
from src.trident import Trident
from sys import exit
import random

pygame.init()


class Controller:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))

        self.maxFish = 3
        self.numberOfFish = 0
        self.earnings = 0
        self.fishes = []
        self.fishCaught = 0
      
        self.clock = pygame.time.Clock()

    def checkCollision(self, trident):
      tridentRect = trident.image.get_rect()
      for fish in self.fishes:
        if tridentRect.colliderect(fish.image.get_rect()):
          print(f"You caught a fish! It's worth ${fish.value}!")  
  
    def mainloop(self):
        self.clock.tick(60)
        loop = "menu"
        run = True
        while run:
            if loop == "menu":
                #self.menuloop()
                if self.menuloop() == "game":
                    loop = "game"
            elif loop == "game":
                result = self.gameloop()
                if result == "retire":
                   loop = "retire"
                if result == "menu":
                    loop = "menu"
            elif loop == "retire":
                if self.retireLoop() == "end":
                  pygame.quit()
                  exit()
                

    def menuloop(self):

        fontStart = pygame.font.Font(None, 70)
        fontTitle = pygame.font.Font(None, 100)
        fontQuit = pygame.font.Font(None, 30)
        rectStartButton = (((200*1.3), (250*1.5)), ((200*1.3), (75*1.5)))
        startHitbox = pygame.Rect(rectStartButton)
        rectQuitButton = (((45*1.3), (350*1.5)), ((60*1.3), (30*1.5)))
        quitButtonHitbox = pygame.Rect(rectQuitButton)
        self.screen.fill("white")
        pygame.draw.rect(self.screen, "palevioletred", rectStartButton)
        pygame.draw.rect(self.screen, "red", rectQuitButton)
        msgStart = fontStart.render("START", True, "black")
        msgTitle = fontTitle.render("Fishing  Game", True, "blue")
        msgQuit = fontQuit.render("QUIT", True, "white")
        self.screen.blit(msgStart, ((220*1.3), (265*1.5)))
        self.screen.blit(msgTitle, ((65*1.3), (35*1.5)))
        self.screen.blit(msgQuit, ((50*1.3), (355*1.5)))
        pygame.display.flip()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = event.pos
                    if startHitbox.collidepoint(clickPos):
                        self.screen.fill("white")
                        pygame.display.flip()
                        pygame.draw.rect(self.screen, "green", rectStartButton)
                        self.screen.blit(msgStart, ((220*1.3), (265*1.5)))
                        pygame.display.flip()
                        pygame.time.wait(350)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        self.screen.fill("white")
                        rectBackToMenu = (((25*1.3), (25*1.5)), ((150*1.3), (50*1.5)))
                        backToMenuHitbox = pygame.Rect(rectBackToMenu)
                        rectLevelButton = (((175*1.3), (125*1.5)), ((250*1.3), (150*1.5)))
                        levelButtonHitbox = pygame.Rect(rectLevelButton)
                        pygame.draw.rect(self.screen, "black", rectBackToMenu)
                        pygame.draw.rect(self.screen, "blue", rectLevelButton)
                        fontBackToMenu = pygame.font.Font(None, 50)
                        msgBackToMenu = fontBackToMenu.render(
                            "MENU", True, "white")
                        self.screen.blit(msgBackToMenu, (50, 35))
                        pygame.display.flip()
                        # also add level select screens once I can be bothered to get to that
                        run2 = True
                        while run2:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    clickPos = event.pos
                                    if backToMenuHitbox.collidepoint(clickPos):
                                        return ("menu")
                                    elif levelButtonHitbox.collidepoint(clickPos):
                                        self.screen.fill("white")
                                        pygame.display.flip()
                                        pygame.time.wait(1000)
                                        return ("game")

                    elif quitButtonHitbox.collidepoint(clickPos):
                        pygame.quit()
                        exit()

    def gameloop(self):
      
        level = Background()
        self.screen.blit(level.image, (0, 0))
        boy = Player(500, 300, self.screen)
        pygame.display.flip()
        trident = Trident()
        run = True
        while run:

          # Buttons, Text

          rectRetireButton = ((700,640),(80,40))
          retireButtonHitbox = pygame.Rect(rectRetireButton)

          # Character Movement
          
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              clickPos = event.pos
              if retireButtonHitbox.collidepoint(clickPos):
                return "retire"
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
              if event.key == pygame.K_LEFT:
                boy.leftPressed = True
                boy.image = pygame.image.load("assets/boysideleft.png")
              if event.key == pygame.K_RIGHT:
                boy.rightPressed = True
                boy.image = pygame.image.load("assets/boyside.png")
              if event.key == pygame.K_UP:
                boy.upPressed = True
                boy.image = pygame.image.load("assets/boyback.png")
              if event.key == pygame.K_DOWN:
                boy.downPressed = True
                boy.image = pygame.image.load("assets/boy.png")
              if event.key == pygame.K_SPACE:
                if trident.state == "ready":
                  trident.throw(self.screen, boy.x, boy.y)
            if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT:
                boy.leftPressed = False
              if event.key == pygame.K_RIGHT:
                boy.rightPressed = False
              if event.key == pygame.K_UP:
                boy.upPressed = False
              if event.key == pygame.K_DOWN:
                boy.downPressed = False

          if boy.y < 150:
            boy.y = 150
          if boy.y > 600:
            boy.y = 600
          if boy.x < 0:
            boy.x = 0
          if boy.x > 800:
            boy.x = 800

          # Fish 

          if self.numberOfFish < self.maxFish:
            self.numberOfFish += 1

          
          if len(self.fishes) < 3:
            for fish in range(self.numberOfFish):
              self.fishes.append(Fish(0, (random.randrange(0,175))))

          
          for fish in self.fishes:
            fishRect = ((fish.x, fish.y),(fish.image.get_size()))
            fishHitbox = pygame.Rect(fishRect)
            if fishHitbox.collidepoint((trident.x, trident.y)):
              self.earnings += fish.value
              self.fishCaught += 1
              self.fishes.remove(fish)
          
          for fish in self.fishes:
            fish.update()

          # Trident

          trident.update()
          
      
          
          self.screen.blit(level.image, (0,0))
          boy.draw(self.screen)

          trident.draw(self.screen)
          
          for fish in self.fishes:
            fish.draw(self.screen)

          #self.checkCollision(trident)
          
          # pygame.draw.rect(self.screen, "red", rectRetireButton)
          # fontRetire = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 30)
          # msgRetire = fontRetire.render("RETIRE", True, "white")
          # self.screen.blit(msgRetire, (700, 640))
          # pygame.display.flip()
          
          boy.update()
          pygame.display.flip()
        
          self.clock.tick(60)

    def retireLoop():  #potential "game over" state to display stats at the end of the game
        print("COngrats you finsihed")
        return "done"

          

def main():
    carp = Controller()
    carp.mainloop()


main()
