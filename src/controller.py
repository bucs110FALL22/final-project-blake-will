import pygame
import background
import fish
import player
from sys import exit

pygame.init()


class Controller:

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 400))

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
        rectStartButton = ((200, 250), (200, 75))
        startHitbox = pygame.Rect(rectStartButton)
        rectQuitButton = ((45, 350), (60, 30))
        quitButtonHitbox = pygame.Rect(rectQuitButton)
        self.screen.fill("white")
        pygame.draw.rect(self.screen, "palevioletred", rectStartButton)
        pygame.draw.rect(self.screen, "red", rectQuitButton)
        msgStart = fontStart.render("START", True, "black")
        msgTitle = fontTitle.render("Fishing  Game", True, "blue")
        msgQuit = fontQuit.render("QUIT", True, "white")
        self.screen.blit(msgStart, (220, 265))
        self.screen.blit(msgTitle, (65, 35))
        self.screen.blit(msgQuit, (50, 355))
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
                        self.screen.blit(msgStart, (220, 265))
                        pygame.display.flip()
                        pygame.time.wait(350)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        self.screen.fill("white")
                        rectBackToMenu = ((25, 25), (150, 50))
                        backToMenuHitbox = pygame.Rect(rectBackToMenu)
                        rectLevelButton = ((175, 125), (250, 150))
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
        level = background.Background()
        level.image.blit(self.screen, (0, 0))
        pygame.display.flip()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

    def endloop(
    ):  #potential "game over" state to display stats at the end of the game
        pass


def main():
    carp = Controller()
    carp.mainloop()


main()
