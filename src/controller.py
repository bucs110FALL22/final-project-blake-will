import pygame
from src.background import Background
from src.fish import Fish
from src.player import Player
from sys import exit

pygame.init()


class Controller:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))

        # sizeList = pygame.display.get_window_size()
        # width = sizeList[0]
        # length = sizeList[1]

        self.clock = pygame.time.Clock()

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
                # if self.gameloop() == "kill":
                #   loop = "done"
                result = self.gameloop()
                if result == "menu":
                    loop = "menu"
            elif loop == "end":
                self.endloop()

    def menuloop(self):

        # sizeList = pygame.display.get_window_size()
        # width = sizeList[0]
        # length = sizeList[1]
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
        run = True
        while run:

          # Character Movement
          
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              exit()
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
                boy.castHook()
              if event.key == pygame.K_SPACE and boy.hook == True:
                boy.catch
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
          self.maxFish = 5
          self.numberOfFish = 0
          self.fishes = []
          
        
          self.screen.fill((12,24,36))
          self.screen.blit(level.image, (0,0))
          boy.draw(self.screen)
        
          boy.update()
          pygame.display.flip()
        
          self.clock.tick(60)
            # for event in pygame.event.get():
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_ESCAPE:
            #           pygame.quit()
            #           exit()
            #         elif event.key == pygame.K_w or pygame.K_UP:
            #           pass
            #         elif event.key == pygame.K_a or pygame.K_LEFT:
            #           pass
            #         elif event.key == pygame.K_d or pygame.K_RIGHT:
            #           pass
            #         elif event.key == pygame.K_s or pygame.K_DOWN:
            #           pass

    def endloop():  #potential "game over" state to display stats at the end of the game
        pass


def main():
    carp = Controller()
    carp.mainloop()


main()
