import pygame
pygame.init()


class Controller:

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 400))

        # sizeList = pygame.display.get_window_size()
        # width = sizeList[0]
        # length = sizeList[1]

        self.mainloop()

    def mainloop(self):
        loop = "menu"
        while True:
            if loop == "menu":
                self.menuloop()
                if self.menuloop() == "game":
                    loop = "game"
            elif loop == "game":
                self.gameloop
                if self.gameloop() == "kill":
                    break
            elif loop == "end":
                self.endloop

    def menuloop(self):

        # sizeList = pygame.display.get_window_size()
        # width = sizeList[0]
        # length = sizeList[1]
        font = pygame.font.Font(None, 70)
        rectStartButton = ((200, 250), (200, 75))
        startHitbox = pygame.Rect(rectStartButton)
        self.screen.fill("white")
        pygame.draw.rect(self.screen, "palevioletred", rectStartButton)
        msgStart = font.render("START", True, "black")
        self.screen.blit(msgStart, (220, 265))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = event.pos
                    if startHitbox.collidepoint(clickPos):
                        return "game"

    def gameloop(self):
        self.screen.fill("black")
        pygame.display.flip()
        print("Good luck!")
        pygame.time.wait(1000)
        return ("kill")

    def endloop(
    ):  #potential "game over" state to display stats at the end of the game
        pass


def main():
    carp = Controller()
    carp.mainloop()


main()
