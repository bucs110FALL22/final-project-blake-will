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

    # def checkCollision(self, trident):
    #   tridentRect = trident.image.get_rect()
    #   for fish in self.fishes:
    #     if tridentRect.colliderect(fish.image.get_rect()):
    #       print(f"You caught a fish! It's worth ${fish.value}!")  
  
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
                if self.retireLoop() == "done":
                  pygame.quit()
                  exit()
                

    def menuloop(self):

        fontStart = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 70)
        fontTitle = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 100)
        fontQuit = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 30)
        rectStartButton = (((260), (375)), ((260), (112.5)))
        startHitbox = pygame.Rect(rectStartButton)
        rectQuitButton = (((58.5), (525)), ((78), (45)))
        quitButtonHitbox = pygame.Rect(rectQuitButton)
        self.screen.fill("white")
        waves = pygame.image.load("assets/waaavey.jpg")
        self.screen.blit(waves, (0, 0))
        pygame.draw.rect(self.screen, "goldenrod", rectStartButton)
        pygame.draw.rect(self.screen, "red", rectQuitButton)
        msgStart = fontStart.render("START", True, "black")
        msgTitle = fontTitle.render("Fishing  Game", True, "navy")
        msgQuit = fontQuit.render("QUIT", True, "white")
        self.screen.blit(msgStart, ((284), (402)))
        self.screen.blit(msgTitle, ((78), (53)))
        self.screen.blit(msgQuit, ((65), (535)))
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
                        self.screen.blit(msgStart, ((284), (402)))
                        pygame.display.flip()
                        pygame.time.wait(350)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        self.screen.fill("white")
                        rectBackToMenu = (((32.5), (37.5)), ((195), (75)))
                        backToMenuHitbox = pygame.Rect(rectBackToMenu)
                        rectLevelButton = (((227.5), (187.5)), ((325), (225)))
                        levelButtonHitbox = pygame.Rect(rectLevelButton)
                        pygame.draw.rect(self.screen, "black", rectBackToMenu)
                        pygame.draw.rect(self.screen, "blue", rectLevelButton)
                        fontBackToMenu = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 60)
                        fontLevelStart = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 50)
                        msgLevelPt1 = fontLevelStart.render("THE", True, "white")
                        msgLevelPt2 = fontLevelStart.render("OCEAN", True, "white")
                        msgBackToMenu = fontBackToMenu.render(
                            "MENU", True, "white")
                        self.screen.blit(msgBackToMenu, (50, 50))
                        self.screen.blit(msgLevelPt1, (340, 260))
                        self.screen.blit(msgLevelPt2, (305, 300))
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

          rectRetireButton = ((670,540),(110,40))
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

          if boy.y < 250:
            boy.y = 250
          if boy.y > 600:
            boy.y = 600
          if boy.x < 0:
            boy.x = 0
          if boy.x > 800:
            boy.x = 800

          # Fish 

          

          
          if len(self.fishes) <= 3:
            #for fish in range(self.numberOfFish):
            self.fishes.append(Fish(5, (random.randrange(0,175))))

          if self.numberOfFish < self.maxFish:
            self.numberOfFish += 1

          
          for fish in self.fishes:
            fishRect = ((fish.x, fish.y),(fish.image.get_size()))
            fishHitbox = pygame.Rect(fishRect)
            if fishHitbox.collidepoint((trident.x, trident.y)) or fishHitbox.collidepoint(trident.x + trident.image.get_width(), trident.y):
              self.earnings += fish.value
              self.fishCaught += 1
              self.fishes.remove(fish)
          
          for fish in self.fishes:
            fish.update()

          # Trident

          trident.update()
          
      
          
          self.screen.blit(level.image, (0,0))
          boy.draw(self.screen)
          fontPoints = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 50)
          msgPoints = fontPoints.render(f"${self.earnings}", True, "white")
          self.screen.blit(msgPoints, (50, 535))
          
          pygame.draw.rect(self.screen, "red", rectRetireButton)
          fontRetire = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 30)
          msgRetire = fontRetire.render("RETIRE", True, "white")
          self.screen.blit(msgRetire, (675 , 550))
          

          trident.draw(self.screen)
          
          for fish in self.fishes:
            fish.draw(self.screen)

         
          
          
          
          boy.update()
          pygame.display.flip()
        
          self.clock.tick(120)

    def retireLoop(self):  #potential "game over" state to display stats at the end of the game
      print("Congrats, you retired successfully!")
      self.screen.fill("black")
      pygame.display.flip()
      pygame.time.wait(500)
      fontText = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 30)
      fontNumbers = pygame.font.Font("assets/EndlessBossBattleRegular-v7Ey.ttf", 85)
      msgCaught = fontText.render("Over your fishing career, you caught a total of", True, "white")
      msgScore = fontText.render("These fish were worth a total value of...", True, "white")
      msgCaughtNum = fontNumbers.render(f"{self.fishCaught} fish!!!", True, "white")
      msgScoreNum = fontNumbers.render(f"${self.earnings}!!!", True, "white")
      msghow2quit = fontText.render("(Press Q to exit the program)", True, "white")
      self.screen.blit(msgCaught, (30,150))
      pygame.display.flip()
      pygame.time.wait(1500)
      self.screen.blit(msgCaughtNum, (215, 200))
      pygame.display.flip()
      pygame.time.wait(1000)
      self.screen.blit(msgScore, (70, 300))
      pygame.display.flip()
      pygame.time.wait(1500)
      self.screen.blit(msgScoreNum, (230, 350))
      pygame.display.flip()
      pygame.time.wait(1000)
      self.screen.blit(msghow2quit, (145, 500))
      pygame.display.flip()
      run = True
      while run:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
              return "done"
          
        
        
        
      

      #return "done"

          

def main():
    carp = Controller()
    carp.mainloop()


main()
