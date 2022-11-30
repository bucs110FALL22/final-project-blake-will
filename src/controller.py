class Controller:

    def __init__(self):
        self.screen = pygame.display.set_mode()

        sizeList = pygame.display.get_window_size()
        width = sizeList[0]
        length = sizeList[1]

        self.mainloop()

    def mainloop(self):
        loop = "menu"
        while True:
            if loop == "menu":
                self.menuloop()
            elif loop == "game":
                self.gameloop
            elif loop == "end":
                self.endloop

    def menuloop(self):
        menu = pygame_menu.menu.Menu()
        menu.add.button("Start")
        pygame.flip()
        while True:
            menu.blit(self.screen)

    def gameloop(self):
        pass

    def endloop(
    ):  #potential "game over" state to display stats at the end of the game
        pass
